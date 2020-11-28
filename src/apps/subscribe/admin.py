from django.contrib import admin

from src.apps.subscribe.models import Subscribe


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "created_at")
    list_display_links = ("pk", "email")
    readonly_fields = ("created_at",)
