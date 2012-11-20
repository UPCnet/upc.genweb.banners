from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class GenwebBannersPortlet(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import upc.genweb.banners
        xmlconfig.file('configure.zcml',
                       upc.genweb.banners,
                       context=configurationContext)
        z2.installProduct(app, 'upc.genweb.banners')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'upc.genweb.banners:default')


GENWEB_BANNERS_PORTLET_FIXTURE = GenwebBannersPortlet()
GENWEB_BANNERS_PORTLET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GENWEB_BANNERS_PORTLET_FIXTURE,),
    name="GenwebBannersPortlet:Integration")
GENWEB_BANNERS_PORTLET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GENWEB_BANNERS_PORTLET_FIXTURE,),
    name="GenwebBannersPortlet:Functional")
