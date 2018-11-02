from django.contrib import admin

from .models.product import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
