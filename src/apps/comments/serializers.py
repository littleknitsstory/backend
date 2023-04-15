from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.apps.comments.models import Comment

User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class CommentListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "text",
            "created_at",
        )


class CommentRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "text",
            "created_at",
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "text",
            "model_type",
            "model_id",
        )
        read_only_fields = [
            "author",
            "model_type",
            "model_id",
        ]

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        validated_data["model_type"] = self.context["request"].query_params.get(
            "model_type", "COMMENT"
        )
        validated_data["model_id"] = self.context["request"].query_params.get(
            "model_id", 0
        )
        return super().create(validated_data)

    def validate(self, data):
        return data


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("text",)
