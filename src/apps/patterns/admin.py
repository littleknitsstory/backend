from django.contrib import admin

from src.apps.patterns.models import Pattern


@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uuid",
        "prompt",
        "author",
    )
    list_display_links = ("uuid",)
    readonly_fields = (
        "uuid",
        "author",
    )
