from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.apps.reactions.models import Reaction
from src.apps.reactions.permissions import IsOwnerOrAdmin
from src.apps.reactions.serializers import (
    ReactionListSerializer,
    ReactionRetrieveSerializer,
    ReactionCreateSerializer,
    ReactionUpdateSerializer,
    ReactionDeletSerializer,
)


class ReactionList(ModelViewSet):
    queryset = Reaction.objects.filter(is_delete=False).prefetch_related("author")
    http_method_names = ["get", "post", "put", "delete"]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ["author", "model_type", "model_id",]
    search_fields = [
        "reaction",
    ]

    permission_classes = (AllowAny, IsAuthenticated, IsOwnerOrAdmin)

    serializer_classes = {
        "list": ReactionListSerializer,
        "retrieve": ReactionRetrieveSerializer,
        "create": ReactionCreateSerializer,
        "update": ReactionUpdateSerializer,
        "delete": ReactionDeletSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, ReactionListSerializer)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy", "delete"]:
            return [IsOwnerOrAdmin()]
        return []

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()
