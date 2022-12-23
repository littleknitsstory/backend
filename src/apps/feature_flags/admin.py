from django.contrib import admin

from src.apps.feature_flags.models import Feature


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "is_active"]
    list_display_links = ("name",)
    actions = ["make_active", "make_not_active"]

    @admin.action(description="Make selected Features active")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Make selected Features not active")
    def make_not_active(self, request, queryset):
        queryset.update(is_active=False)
