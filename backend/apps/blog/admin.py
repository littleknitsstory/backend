from django.contrib import admin

from apps.blog.models import Article
from core.mixins.mixin import AdminBaseMixin


@admin.register(Article)
class ArticleAdmin(AdminBaseMixin):
    filter_horizontal = ('tags',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'is_active', 'content', 'image_preview', 'author', 'tags')
        }),
        ('SEO', {
            'fields': ('title_seo', 'meta_keywords', 'meta_description', 'image_alt')
        }),
    )
