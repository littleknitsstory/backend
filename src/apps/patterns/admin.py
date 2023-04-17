from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from src.apps.patterns.models import Pattern


@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ("id", "pattern_number", "prompt", "author")
    list_display_links = ("pattern_number",)
    readonly_fields = ("pattern_number", "author")
