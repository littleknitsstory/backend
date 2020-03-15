from django.contrib import admin

from src.apps.reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    list_filter = ["created_at", "author"]
    search_fields = ["comment"]
    fields = [
        "title",
        "author",
        "image_preview",
        "image_alt",
        "comment",
        "email",
        "rating",
        "is_active",
    ]
