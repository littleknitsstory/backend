from django.contrib import admin

from src.apps.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "author",
        "model_type",
        "model_id",
        "is_deleted",
    )
