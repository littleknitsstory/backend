from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import ugettext_lazy as _

from src.core.mixins.mixin import AdminBaseMixin
from .models import OrderCart
from .models.category import Category
from .models.product import Product, ProductPhoto, ProductColor


@admin.register(Category)
class CategoryAdmin(TranslationAdmin, AdminBaseMixin):
    list_display = ("title", "slug", "meta_description", "created_at", "update_at")
    fieldsets = (
        (_("Content"), {"fields": ("title",)}),
        (_("Main"), {"fields": ("slug",)}),
        (_("SEO"), {"fields": ("title_seo", "meta_keywords", "meta_description",)}),
    )


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = (
        "photo",
        "photo_alt",
    )


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ("color",)


@admin.register(Product)
class ProductAdmin(TranslationAdmin, AdminBaseMixin):
    inlines = [
        ProductPhotoInline,
    ]
    group_fieldsets = True
    list_display = ("code", "slug", "is_active", "update_at")
    filter_horizontal = ("categories", "colors")
    fieldsets = (
        (_("Title"), {"fields": ("title",)}),
        (
            _("Main"),
            {
                "fields": (
                    "code",
                    "slug",
                    "is_active",
                    "sale",
                    "price",
                    "image_preview",
                    "author",
                    "categories",
                    "colors",
                )
            },
        ),
        (_("Description"), {"fields": ("description",)}),
        (
            _("Feature"),
            {"fields": ("type_product", "material", "included", "height", "weight")},
        ),
        (
            _("SEO"),
            {"fields": ("title_seo", "meta_keywords", "meta_description", "image_alt")},
        ),
    )


@admin.register(OrderCart)
class OrderCartAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "update_at", "created_at")
    filter_horizontal = ("products",)
    fieldsets = (
        (_("Status"), {"fields": ("status", "update_at", "created_at")}),
        (_("Info"), {"fields": ("email", "phone", "address", "comments", )}),
        (_("Products"), {"fields": ("products", )}),
    )
