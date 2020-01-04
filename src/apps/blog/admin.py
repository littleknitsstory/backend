from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline, TranslationAdmin

from src.apps.blog.models import Article, Tag
from src.core.mixins.mixin import AdminBaseMixin


# class TagInline(TranslationTabularInline):
#     model = Tag

#
# @admin.register(Article)
# class ArticleAdmin(AdminBaseMixin):
#     # filter_horizontal = ('tags',)
#     # inlines = [TagInline, ]
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'slug', 'is_active', 'content', 'image_preview', 'author',)
#         }),
#         ('SEO', {
#             'fields': ('title_seo', 'meta_keywords', 'meta_description', 'image_alt')
#         }),
#     )
