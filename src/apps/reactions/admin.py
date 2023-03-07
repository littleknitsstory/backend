from django.contrib import admin

from src.apps.reactions.models import Reaction


@admin.register(Reaction)
class REactionAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "model_type", "model_id", "is_deleted")
