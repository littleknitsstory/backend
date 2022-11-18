from django.contrib import admin

from src.apps.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "to_model", "model_id", "is_deleted")