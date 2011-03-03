# -*- coding: utf-8 -*-

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.ATContentTypes.content.folder import ATFolder

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




