from rest_framework import serializers
from django.db import transaction

from src.apps.account.models import User
from src.apps.comments.models import Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class CommentListCreateSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "text",
            "created_at",
            "model_type",
            "model_id",
        )
        read_only_fields = [
            "author",
            "model_type",
            "model_id",
        ]

    @transaction.atomic
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def validate(self, data):
        return data


# class CommentCreateSerializer(serializers.ModelSerializer):
#     """Создание комментариев"""
#     author = AuthorSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = (
#             "id",
#             "author",
#             "text",
#             "model_type",
#             "model_id",
#         )
#         read_only_fields = ["author", "model_type", "model_id", ]

# def create(self, validated_data):
#         validated_data["author"] = self.context["request"].user
#         validated_data["model_type"] = self.context["request"].query_params.get("model_type", "REACTION")
#         validated_data["model_id"] = self.context["request"].query_params.get("model_id", 0)
#         return super().create(validated_data)

#     def validate(self, data):
#         return data


class CommentUpdateSerializer(serializers.ModelSerializer):
    """редактирование комментариев"""

    author = AuthorSerializer(read_only=True)

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

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.text = validated_data.get("text", instance.text)
        instance.model_type = validated_data.get("model_type", instance.model_type)
        instance.save()
        return instance

    def validate(self, data):
        return data
