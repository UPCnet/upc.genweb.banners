import unittest2 as unittest

from zope.component import getUtility, getMultiAdapter

from plone.testing.z2 import Browser
from plone.app.testing import TEST_USER_ID, TEST_USER_NAME
from plone.app.testing import login, logout
from plone.app.testing import setRoles

from plone.portlets.interfaces import IPortletType
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.interfaces import IPortletRenderer

from plone.app.portlets.storage import PortletAssignmentMapping

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType

from upc.genweb.banners.portlets import bannersportlet

from upc.genweb.banners.testing import GENWEB_BANNERS_PORTLET_INTEGRATION_TESTING


class IntegrationTest(unittest.TestCase):

    layer = GENWEB_BANNERS_PORTLET_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory('Folder', 'folder', title="A folder")
        self.folder = self.portal['folder']

    def test_content_types(self):
        self.assertRaises(ValueError, self.portal.invokeFactory, 'Banner', 'b1', title="A banner")
        _createObjectByType('BannerContainer', self.portal, 'bannerFolder')
        self.portal['bannerFolder'].invokeFactory('Banner', 'b1', title="The banner")
        banner = self.portal['bannerFolder']['b1']
        banner.edit(Obrirennovafinestra=True)
        self.assertEquals(banner.Obrirennovafinestra, True)
        self.assertEquals(banner.obrirEnFinestraNova(), True)

    def test_portlet_type_registered(self):
        portlet = getUtility(IPortletType, name='upc.genweb.banners.portlet')
        self.assertEquals(portlet.addview, 'upc.genweb.banners.portlet')

    def test_interfaces(self):
        # TODO: Pass any keyword arguments to the Assignment constructor
        portlet = bannersportlet.Assignment()
        self.failUnless(IPortletAssignment.providedBy(portlet))
        self.failUnless(IPortletDataProvider.providedBy(portlet.data))

    def test_invoke_add_view(self):
        portlet = getUtility(IPortletType, name='upc.genweb.banners.portlet')
        mapping = self.portal.restrictedTraverse(
            '++contextportlets++plone.leftcolumn')
        for m in mapping.keys():
            del mapping[m]
        addview = mapping.restrictedTraverse('+/' + portlet.addview)

        # TODO: Pass a dictionary containing dummy form inputs from the add
        # form.
        # Note: if the portlet has a NullAddForm, simply call
        # addview() instead of the next line.
        addview.createAndAdd(data={})

        self.assertEquals(len(mapping), 1)
        self.failUnless(isinstance(mapping.values()[0],
                                   bannersportlet.Assignment))

    def test_invoke_edit_view(self):
        # NOTE: This test can be removed if the portlet has no edit form
        mapping = PortletAssignmentMapping()
        request = self.folder.REQUEST

        mapping['foo'] = bannersportlet.Assignment()
        editview = getMultiAdapter((mapping['foo'], request), name='edit')
        self.failUnless(isinstance(editview, bannersportlet.EditForm))

    def test_obtain_renderer(self):
        context = self.folder
        request = self.folder.REQUEST
        view = self.folder.restrictedTraverse('@@plone')
        manager = getUtility(IPortletManager, name='plone.rightcolumn',
                             context=self.portal)

        # TODO: Pass any keyword arguments to the Assignment constructor
        assignment = bannersportlet.Assignment()

        renderer = getMultiAdapter(
            (context, request, view, manager, assignment), IPortletRenderer)
        self.failUnless(isinstance(renderer, bannersportlet.Renderer))

    def renderer(self, context=None, request=None, view=None, manager=None,
                 assignment=None):
        context = context or self.folder
        request = request or self.folder.REQUEST
        view = view or self.folder.restrictedTraverse('@@plone')
        manager = manager or getUtility(
            IPortletManager, name='plone.rightcolumn', context=self.portal)

        # TODO: Pass any default keyword arguments to the Assignment
        # constructor.
        assignment = assignment or bannersportlet.Assignment()
        return getMultiAdapter((context, request, view, manager, assignment),
                               IPortletRenderer)

    def test_render(self):
        # TODO: Pass any keyword arguments to the Assignment constructor.
        r = self.renderer(context=self.portal,
                          assignment=bannersportlet.Assignment())
        r = r.__of__(self.folder)
        r.update()
        #self.assertEqual(r.getAltAndTitle('Titol'), u"Titol, (open link in a new window)")

        _createObjectByType('BannerContainer', self.portal, 'bannerFolder')
        self.portal['bannerFolder'].invokeFactory('Banner', 'b1', title="The banner")
        banner = self.portal['bannerFolder']['b1']
        banner.edit(Obrirennovafinestra=True)
        pw = getToolByName(self.portal, 'portal_workflow')
        pw.setDefaultChain('simple_publication_workflow')
        pw.setChainForPortalTypes(('Banner',), 'simple_publication_workflow')
        pw.doActionFor(banner, 'publish')

        r.render()
