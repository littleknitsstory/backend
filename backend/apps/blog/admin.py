from django.contrib import admin

from apps.blog.models import Article
from core.mixin import AdminBaseMixin


@admin.register(Article)
class ArticleAdmin(AdminBaseMixin):
    pass
