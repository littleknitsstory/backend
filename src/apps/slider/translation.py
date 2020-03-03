from modeltranslation.translator import TranslationOptions, register
from src.apps.slider.models import Slider


@register(Slider)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title", "sub_title")
