from modeltranslation.translator import translator

from .models import Unit, Item
from ecom.utils.translation import NameDescriptionTranslationOptions, NameTranslationOptions

translator.register(Unit, NameTranslationOptions)
translator.register(Item, NameDescriptionTranslationOptions)

