# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

schema = Schema((

    ImageField(
        name='Imatge',
        widget=ImageField._properties['widget'](
            label='Image',
            label_msgid='upc.genweb.banners_label_Imatge',
            i18n_domain='upc.genweb.banners',
        ),
        storage=AttributeStorage(),
    ),
    StringField(
        name='URLdesti',
        widget=StringField._properties['widget'](
            label='Urldesti',
            description="You must include http:// at the beginning to make an external link",            
            label_msgid='upc.genweb.banners_label_URLdesti',
            description_msgid='upc.genweb.banners_help_descripcion',            
            i18n_domain='upc.genweb.banners',
        ),
    ),
    BooleanField(
        name='Obrirennovafinestra',
        widget=BooleanField._properties['widget'](
            label='Open in a new window',
            label_msgid='upc.genweb.banners_label_Obrirennovafinestra',
            i18n_domain='upc.genweb.banners',
        ),
    ),
),
)

Banner_schema = BaseSchema.copy() + \
    schema.copy()

class Banner(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()
    implements(interfaces.IBanner)

    meta_type = 'Banner'
    _at_rename_after_creation = True

    schema = Banner_schema




