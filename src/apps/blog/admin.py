from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline, TranslationAdmin
from django.utils.translation import ugettext_lazy as _

from src.apps.blog.models import Article, Tag
from src.core.mixins.mixin import AdminBaseMixin


@admin.register(Tag)
class TagAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    fieldsets = (
        (None, {"fields": ("title", "slug",)}),
        (_("SEO"), {"fields": ("title_seo", "meta_keywords", "meta_description")}),
    )


@admin.register(Article)
class ArticleAdmin(TranslationAdmin, AdminBaseMixin):
    list_display_links = ("title",)
    filter_horizontal = ("tags",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "is_active",
                    "image_preview",
                    "author",
                    "tags",
                )
            },
        ),
        (_("Content"), {"fields": ("content",)}),
        (
            _("SEO"),
            {"fields": ("title_seo", "meta_keywords", "meta_description", "image_alt")},
        ),
    )
