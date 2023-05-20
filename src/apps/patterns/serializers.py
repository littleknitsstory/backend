from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.apps.patterns.models import Pattern

User = get_user_model()


class AuthorPromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "avatar",
            "first_name",
            "last_name",
        )


class PatternSerializer(serializers.ModelSerializer):
    prompt = serializers.CharField()
    author = AuthorPromptSerializer(read_only=True)

    class Meta:
        model = Pattern
        fields = (
            "uuid",
            "prompt",
            "author",
            "created_up",
        )


class MessageSerializer(serializers.Serializer):
    content = serializers.CharField()


class ChoicesSerializer(serializers.Serializer):
    message = MessageSerializer()


class DataSerializer(serializers.Serializer):
    choices = ChoicesSerializer(many=True)
