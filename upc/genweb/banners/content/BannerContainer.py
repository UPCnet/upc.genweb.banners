# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.ATContentTypes.content.folder import ATFolder
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from upc.genweb.banners.config import *

schema = Schema((

),
)

BannerContainer_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()


class BannerContainer(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IBannerContainer)

    meta_type = 'BannerContainer'
    _at_rename_after_creation = True

    schema = BannerContainer_schema

registerType(BannerContainer, PROJECTNAME)
