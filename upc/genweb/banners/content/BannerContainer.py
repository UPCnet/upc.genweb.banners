# -*- coding: utf-8 -*-
#
# File: BannerContainer.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.0
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.ATContentTypes.content.folder import ATFolder
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from upc.genweb.banners.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BannerContainer_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BannerContainer(ATFolder):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IBannerContainer)

    meta_type = 'BannerContainer'
    _at_rename_after_creation = True

    schema = BannerContainer_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(BannerContainer, PROJECTNAME)
# end of class BannerContainer

##code-section module-footer #fill in your manual code here
##/code-section module-footer



