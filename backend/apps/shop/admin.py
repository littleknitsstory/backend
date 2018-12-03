from django.contrib import admin
from django import forms
from core.mixin import AdminBaseMixin
from .models.category import Category
from .models.product import Product
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField


@admin.register(Category)
class CategoryAdmin(AdminBaseMixin):
    list_display = ['title', 'slug', 'description', 'created_at', 'update_at']


# class ProductAdminForm(forms.ModelForm):
#
#     description = forms.CharField(widget=CKEditorWidget())
#
#     class Meta:
#         model = Product
#         fields = '__all__'


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
    # form = ProductAdminForm


admin.site.register(Product, ProductAdmin)

