from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.apps.comments.models import Comment
from src.apps.comments.permissions import IsOwnerOrAdmin
from src.apps.comments.serializers import (
    CommentListSerializer,
    CommentRetrieveSerializer,
    CommentCreateSerializer,
    CommentUpdateSerializer,
)


class CommentList(ModelViewSet):
    queryset = Comment.objects.filter(is_deleted=False).prefetch_related("author")
    http_method_names = ["get", "post", "put", "delete"]
    lookup_field = "id"
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ["author", "model_type", "model_id", "created_at", "updated_at"]
    search_fields = [
        "text",
    ]
    ordering_fields = [
        "created_at",
    ]
    permission_classes = (AllowAny, IsAuthenticated, IsOwnerOrAdmin)

    serializer_classes = {
        "list": CommentListSerializer,
        "retrieve": CommentRetrieveSerializer,
        "create": CommentCreateSerializer,
        "update": CommentUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, CommentCreateSerializer)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return []

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
