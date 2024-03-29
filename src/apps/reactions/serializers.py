from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import serializers

from src.apps.reactions.models import Reaction

User = get_user_model()


class AuthorReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )


class ReactionListSerializer(serializers.ModelSerializer):
    author = AuthorReactionSerializer(read_only=True)
    reaction = serializers.SerializerMethodField()

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
            "reaction",
            "model_type",
            "model_id",
        )

    def get_reaction(self, obj):
        return (
            Reaction.objects.filter(id=obj.id)
            .values("reaction")
            .annotate(total=Count("id"))
        )


class ReactionRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorReactionSerializer(read_only=True)

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
            "reaction",
            "model_type",
            "model_id",
        )


class ReactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
            "reaction",
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


class ReactionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ("reaction",)
