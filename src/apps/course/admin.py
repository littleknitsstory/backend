from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from src.apps.course.models import Course, Step, CourseContent
from src.apps.blog.models import Article, Tag
import nested_admin


@admin.register(CourseContent)
class TocArticleInline(nested_admin.NestedModelAdmin):
    list_display = (
        "model_id",
        "model_type",
    )
    fieldsets = ((None, {"fields": ("model_id", "model_type")}),)


class TocSectionInline(nested_admin.NestedStackedInline):
    model = Step
    sortable_field_name = "id"
    # inlines = [TocArticleInline]


@admin.register(Course)
class CourseAdmin(nested_admin.NestedModelAdmin):
    list_display = ("title",)
    fieldsets = ((None, {"fields": ("title",)}),)

    inlines = [TocSectionInline]


# Example:
# class TocArticleInline(nested_admin.NestedStackedInline):
#     model = TocArticle
#     sortable_field_name = "position"
#
# class TocSectionInline(nested_admin.NestedStackedInline):
#     model = TocSection
#     sortable_field_name = "position"
#     inlines = [TocArticleInline]
#
# class TableOfContentsAdmin(nested_admin.NestedModelAdmin):
#     inlines = [TocSectionInline]
