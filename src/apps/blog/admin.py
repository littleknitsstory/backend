from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from src.apps.blog.models.bookmark import Bookmark
from src.apps.blog.models.models import Article, Tag, ArticleContent


@admin.register(Tag)
class TagAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    fieldsets = ((None, {"fields": ("title", "slug")}),)


@admin.register(ArticleContent)
class BlockContentAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "image",
        "image_alt",
    )
    fieldsets = ((None, {"fields": ("text", "image", "image_alt")}),)


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    save_as = True
    save_on_top = True
    list_display = ("pk", "title", "slug")
    list_display_links = ("title",)
    filter_horizontal = ("tags", "contents")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "description",
                    "slug",
                    "is_active",
                    # "image_preview",
                    "author",
                    "tags",
                    "contents",
                )
            },
        ),
        # (_("Content"), {"fields": ("content",)}),
        # (
        #     _("SEO"),
        #     {
        #         "fields": (
        #             "meta_title",
        #             "meta_keywords",
        #             "meta_description",
        #             "image_alt",
        #         )
        #     },
        # ),
    )


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "article",
    )
    list_display_links = ("article",)
