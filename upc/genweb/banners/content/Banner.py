# -*- coding: utf-8 -*-
#
# File: Banner.py
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

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from upc.genweb.banners.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ImageField(
        name='Imatge',
        widget=ImageField._properties['widget'](
            label='Imatge',
            label_msgid='upc.genweb.banners_label_Imatge',
            i18n_domain='upc.genweb.banners',
        ),
        storage=AttributeStorage(),
    ),
    StringField(
        name='URLdesti',
        widget=StringField._properties['widget'](
            label='Urldesti',
            label_msgid='upc.genweb.banners_label_URLdesti',
            i18n_domain='upc.genweb.banners',
        ),
    ),
    BooleanField(
        name='Obrirennovafinestra',
        widget=BooleanField._properties['widget'](
            label='Obrirennovafinestra',
            label_msgid='upc.genweb.banners_label_Obrirennovafinestra',
            i18n_domain='upc.genweb.banners',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Banner_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Banner(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IBanner)

    meta_type = 'Banner'
    _at_rename_after_creation = True

    schema = Banner_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Banner, PROJECTNAME)
# end of class Banner

##code-section module-footer #fill in your manual code here
##/code-section module-footer



