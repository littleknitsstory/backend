from modeltranslation.translator import TranslationOptions, register, translator
from src.apps.blog.models import Tag, Article


@register(Tag)
class TagsTranslationOptions(TranslationOptions):
    fields = ("title", "meta_title", "meta_keywords", "meta_description")


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ("title", "content", "meta_title", "meta_keywords", "meta_description")
