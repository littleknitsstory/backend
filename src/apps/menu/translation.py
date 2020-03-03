from modeltranslation.translator import TranslationOptions, register
from src.apps.menu.models import MenuItems


@register(MenuItems)
class MenuTranslationOptions(TranslationOptions):
    fields = ("name",)
