from rest_framework import serializers

from src.apps.account.models import User
from src.apps.reactions.models import Reaction


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class ReactionListSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer(read_only=True)

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
            "text",
            "created_at",
        )


class ReactionRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorsSerializer(read_only=True)

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
            "text",
            "created_at",
        )


class ReactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
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
            "model_type", "REACTION"
        )
        validated_data["model_id"] = self.context["request"].query_params.get(
            "model_id", 0
        )
        return super().create(validated_data)

    def validate(self, data):
        return data


class ReactionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ("text",)
