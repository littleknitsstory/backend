from django.contrib import admin

from src.apps.patterns.models import Pattern


@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pattern_uuid",
        "prompt",
        "author",
    )
    list_display_links = ("pattern_uuid",)
    readonly_fields = (
        "pattern_uuid",
        "author",
    )
