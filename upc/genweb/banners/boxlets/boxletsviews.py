from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from Products.CMFPlone import PloneMessageFactory as _
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName

from upc.genweb.banners.portlets.bannersportlet import Renderer as banners_render

class banners(BrowserView, banners_render):
    __call__ = ViewPageTemplateFile('banners.pt')
    
    def _data(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        limit = 5
        state = 'published'
        return catalog(portal_type='Banner',
                       review_state=state,
                       sort_limit=limit)[:limit]
    