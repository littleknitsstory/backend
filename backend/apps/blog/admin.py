from django.contrib import admin

from apps.blog.models import Article
from core.mixin import AdminBaseMixin


@admin.register(Article)
class ArticleAdmin(AdminBaseMixin):
    filter_horizontal = ('tags',)
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'active', 'content', 'image_preview', 'author', 'tags')
        }),
        ('SEO', {
            'fields': ('title_seo', 'keywords', 'description', 'image_alt')
        }),
    )
