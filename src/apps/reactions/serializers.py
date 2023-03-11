from rest_framework import serializers
from rest_framework.response import Response

from src.apps.account.models import User
from .models import Reaction
from . import services


class AuthorLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")


class ReactionListSerializer(serializers.ModelSerializer):
    author = AuthorLikeSerializer(read_only=True)

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
        )


class ReactionRetrieveSerializer(serializers.ModelSerializer):
    author = AuthorLikeSerializer(read_only=True)

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
        )


class ReactionCreateSerializer(serializers.ModelSerializer):
    def create(self, request, pk=None):
        obj = self.get_object()
        services.add_reactions(obj, request.user)
        return Response()

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
            "model_type",
            "model_id",
        )
        read_only_fields = [
            "author",
            "model_type",
            "model_id",
        ]


class ReactionDeleteSerializer(serializers.ModelSerializer):
    def delete(self, request, pk=None):
        obj = self.get_object()
        services.remove_reactions(obj, request.user)
        return Response()

    class Meta:
        model = Reaction
        fields = (
            "id",
            "author",
            "model_type",
            "model_id",
        )
        read_only_fields = [
            "author",
            "model_type",
            "model_id",
        ]
