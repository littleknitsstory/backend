from modeltranslation.translator import TranslationOptions, register
from src.apps.shop.models import Category, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title", "meta_title", "meta_keywords", "meta_description")


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
        "type_product",
        "material",
        "included",
        "meta_title",
        "meta_keywords",
        "meta_description",
    )
