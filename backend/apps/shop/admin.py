from django.contrib import admin

from core.mixin import AdminBaseMixin
from .models.category import Category
from .models.product import Product


@admin.register(Category)
class CategoryAdmin(AdminBaseMixin):
    list_display = ['title', 'slug', 'description', 'created_at', 'update_at']


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'slug', 'description', 'keywords', 'price', 'active',
        'created_at', 'update_at'
    ]
    filter_horizontal = ('tags', 'category')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'active', 'price', 'image_preview', 'author', 'tags', 'category')
        }),
        ('SEO', {
            'fields': ('title_seo', 'keywords', 'description', 'image_alt')
        }),
    )


admin.site.register(Product, ProductAdmin)

