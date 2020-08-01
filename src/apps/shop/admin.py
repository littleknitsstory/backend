from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import gettext_lazy as _

from src.core.mixins.mixin import AdminBaseMixin
from .models import OrderCart, OrderCartItem
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
        "image_preview",
        "image_alt",
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
    list_display = ("id", "code", "slug", "is_active", "update_at")
    list_display_links = ("code", "slug")
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
                    "count",
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


class OrderCartItemInline(admin.TabularInline):
    model = OrderCartItem
    extra = 0
    readonly_fields = ("item_total_cost",)
    show_change_link = True


@admin.register(OrderCart)
class OrderCartAdmin(admin.ModelAdmin):
    list_display = ("id", "order_number", "status", "update_at", "created_at")
    list_display_links = ("order_number",)
    inlines = [
        OrderCartItemInline,
    ]
    readonly_fields = ("update_at", "created_at", "order_number", "order_total_cost")
    fieldsets = (
        (
            _("Status"),
            {
                "fields": (
                    "order_number",
                    "order_total_cost",
                    "status",
                    "update_at",
                    "created_at",
                )
            },
        ),
        (_("Info"), {"fields": ("email", "phone", "address", "comments",)}),
    )


@admin.register(OrderCartItem)
class OrderCartItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "order_cart",
        "product",
        "amount",
    )
    fieldsets = ((_("Info"), {"fields": ("order_cart", "product", "amount")}),)
