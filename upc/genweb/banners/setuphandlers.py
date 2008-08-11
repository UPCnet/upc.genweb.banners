def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('upc.genweb.banners_various.txt') is None:
        return
    
    from Products.CMFPlone.utils import _createObjectByType
    portal = context.getSite()
        
    if not getattr(portal,'banners',False):
        _createObjectByType('BannerContainer', portal, 'banners')  
