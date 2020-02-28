from rest_framework import serializers

from src.apps.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'title',
            'author',
            'comment',
            'rating',
            'image_preview'
        )
