from modeltranslation.translator import TranslationOptions, register
from src.apps.shop.models import Category, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'title_seo', 'meta_keywords', 'meta_description')
    
    
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'type_product', 'material', 'included',
              'title_seo', 'meta_keywords', 'meta_description')
