from modeltranslation.translator import TranslationOptions, register

from src.apps.blog.models.models import Tag, Article


@register(Tag)
class TagsTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ("title", "content", "meta_title", "meta_keywords", "meta_description")
