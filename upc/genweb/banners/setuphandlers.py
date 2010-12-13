# -*- coding: utf-8 -*-
def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('upc.genweb.banners_various.txt') is None:
        return
#
#    la creacio de continguts s'ha centralitzat al paquet upc.genwebupc, per fer-la language-aware
#
#    from Products.CMFPlone.utils import _createObjectByType, getToolByName
#    portal = context.getSite()
#    
#    workflowTool = getToolByName(portal, "portal_workflow")
#            
#    if not getattr(portal,'banners',False):
#        _createObjectByType('BannerContainer', portal, 'banners')  
#        portal['banners'].setExcludeFromNav(True)
#        portal['banners'].setTitle('Banners')
#        portal['banners'].reindexObject()
#        workflowTool.doActionFor(portal.banners, "publish")