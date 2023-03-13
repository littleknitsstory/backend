from rest_framework import serializers

from src.apps.account.models import User
from src.apps.reactions.models import Reaction
from rest_framework.response import Response
from . import services


class AuthorReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class ReactionListSerializer(serializers.ModelSerializer):
    author = AuthorReactionSerializer(read_only=True)

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
            "reaction",
        )


class ReactionRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorReactionSerializer(read_only=True)

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
            "reaction",
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

    def create(self, request, pk=None):
        obj = self.get_object()
        services.add_reactions(obj, request.user)
        return Response()


class ReactionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ("reaction",)
