from django.contrib import admin

from src.apps.blog.models import Article
from src.core.mixins.mixin import AdminBaseMixin


@admin.register(Article)
class ArticleAdmin(AdminBaseMixin):
    pass
    # filter_horizontal = ('tags',)

    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'slug', 'is_active', 'content', 'image_preview', 'author', 'tags')
    #     }),
    #     ('SEO', {
    #         'fields': ('title_seo', 'meta_keywords', 'meta_description', 'image_alt')
    #     }),
    # )
