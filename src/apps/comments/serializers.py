from rest_framework import serializers

from src.apps.comments.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "text",
            "created_at",
            "updated_at",
            "to_model",
            "model_id",
            "is_deleted",
        )


class CommentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

