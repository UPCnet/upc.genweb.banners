from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from Products.CMFPlone import PloneMessageFactory as _
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName

from upc.genweb.banners.portlets.bannersportlet import Renderer as banners_render

class banners(BrowserView, banners_render):
    __call__ = ViewPageTemplateFile('banners.pt')

    def getBanners(self):
        return self._data()
            
    def _data(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        limit = 5
        state = ['published','intranet']
        banner_container = catalog.searchResults(portal_type='BannerContainer',
                                                 review_state=state)
        if banner_container:
            return catalog(portal_type='Banner',
                       review_state=state,
                       path=banner_container[0].getPath(),
                       sort_limit=limit)[:limit]
        else:
            return []
    
