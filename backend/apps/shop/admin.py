from django.contrib import admin

from core.mixin import AdminBaseMixin
from .models.category import Category
from .models.product import Product


@admin.register(Category)
class CategoryAdmin(AdminBaseMixin):
    list_display = ['title', 'slug', 'description', 'created_at', 'update_at']


@admin.register(Product)
class ProductAdmin(AdminBaseMixin):
    list_display = [
        'title', 'slug', 'description', 'keywords', 'price', 'active',
        'created_at', 'update_at'
    ]
