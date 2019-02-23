from django.contrib import admin

from core.mixin.mixin import AdminBaseMixin
from .models.category import Category
from .models.product import Product


@admin.register(Category)
class CategoryAdmin(AdminBaseMixin):
    list_display = ['title', 'slug', 'meta_description', 'created_at', 'update_at']


@admin.register(Product)
class ProductAdmin(AdminBaseMixin):
    list_display = [
        'title', 'slug', 'meta_description', 'meta_keywords', 'price', 'is_active',
        'created_at', 'update_at'
    ]
    filter_horizontal = ('tags', 'category')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'is_active', 'price', 'sale',
                       'image_preview', 'author', 'tags', 'category')
        }),
        ('SEO', {
            'fields': ('title_seo', 'meta_keywords', 'meta_description', 'image_alt')
        }),
    )


