from random import randint

from etxt_api import ApiClient
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from src import settings
from src.apps.blog.models import Article, Tag


@admin.register(Tag)
class TagAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    fieldsets = (
        (None, {"fields": ("title", "slug")}),
        (_("SEO"), {"fields": ("title_seo", "meta_keywords", "meta_description")}),
    )


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    save_as = True
    save_on_top = True
    list_display = ("pk", "title", "slug", "is_active")
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
    actions = ["make_active", "make_not_active"]

    def get_etxt_article(self, request):
        client = ApiClient(settings.ETXT_TOKEN, settings.ETXT_API_PASS)
        art_list = client.article_list(text="вязать")
        if "error" in art_list:
            self.message_user(request, "Error: " + art_list["error"])
            return
        if len(art_list) == 0:
            self.message_user(request, "No Articles found")
            return
        num = randint(0, len(art_list)-1)
        Article.objects.create(title=art_list[num]["title"], author=request.user)

    def changelist_view(self, request, extra_context=None):
        if "etxt" in request.GET:
            self.get_etxt_article(request)
        return super().changelist_view(request)

    @admin.action(description="Make selected Articles active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Make selected Articles not active")
    def make_not_active(self, request, queryset):
        queryset.update(is_active=False)
