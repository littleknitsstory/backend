from rest_framework import serializers

from src.apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    image_preview = serializers.CharField(source="get_image")

    class Meta:
        model = Review
        fields = ("title", "author", "comment", "rating", "image_preview")
