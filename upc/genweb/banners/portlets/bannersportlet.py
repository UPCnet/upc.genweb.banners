# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope.interface import implements
from zope.component.hooks import getSite

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('upc.genweb.banners')


class IBannersPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    count = schema.Int(title=_(u'Number of banners to display'),
                       description=_(u'How many banners to list.'),
                       required=True,
                       default=5,
                       min=5,
                       max=7)

    # GW4.2 Fridge
    # state = schema.Tuple(title=_(u"Workflow state"),
    #                      description=_(u"Items in which workflow state to show."),
    #                      default=('published', ),
    #                      required=True,
    #                      value_type=schema.Choice(
    #                          vocabulary="plone.app.vocabularies.WorkflowStates")
    #                      )


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IBannersPortlet)

    def __init__(self, count=5, state=('published', )):
        self.count = count
        # self.state = state

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return _(u"Genweb banners")


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('bannersportlet.pt')

    def portal_url(self):
        return self.portal().absolute_url()

    def portal(self):
        return getSite()

    def getBanners(self):
        catalog = getToolByName(self.portal(), 'portal_catalog')
        limit = self.data.count
        # state = self.data.state
        return catalog.searchResults(portal_type='Banner',
                                     review_state=['published', 'intranet'],
                                     sort_on='getObjPositionInParent',
                                     sort_limit=limit)[:limit]

    def getAltAndTitle(self, altortitle):
        """ Funcio que extreu idioma actiu i afegeix al alt i al title de les imatges del banner
            el literal Obriu l'enllac en una finestra nova.
        """
        return '%s, %s' % (altortitle.decode('utf-8'),
            self.portal().translate(_('obrir_link_finestra_nova', default=u"(obriu en una finestra nova)")))


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IBannersPortlet)
    label = _(u"Add banners portlet")
    description = _(u"This portlet displays the site banners.")

    def create(self, data):
        return Assignment(count=data.get('count', 5), state=data.get('state', ('published',)))


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IBannersPortlet)
    label = _(u"Edit banners portlet")
    description = _(u"This portlet displays the site banners.")
