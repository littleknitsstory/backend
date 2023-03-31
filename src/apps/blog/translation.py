from modeltranslation.translator import TranslationOptions, register, translator
from src.apps.blog.models import Tag, Article


@register(Tag)
class TagsTranslationOptions(TranslationOptions):
    fields = ("title", "title_seo", "meta_keywords", "meta_description")


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ("title", "description", "content", "title_seo", "meta_keywords", "meta_description")
