from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import generics

from src.apps.comments.models import Comment
from src.apps.comments.permissions import IsOwnerOrAdmin

from src.apps.comments.serializers import (
    CommentListCreateSerializer,
    CommentUpdateSerializer,
   # CommentCreateSerializer
)


class CommentList(generics.ListAPIView, generics.CreateAPIView ):
    queryset = Comment.objects.filter(is_deleted=False).prefetch_related("author")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_fields = ["author", "model_type", "model_id", "created_at", "updated_at"]
    search_fields = ['text', ]
    ordering_fields = ['created_at', ]
    permission_classes = (AllowAny,)
    serializer_class = CommentListCreateSerializer

    
# class CommentCreate(generics.CreateAPIView):
#     queryset = Comment.objects.filter(is_deleted=False).prefetch_related("author")
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
#     filterset_fields = ["author", "model_type", "model_id", "created_at", "updated_at"]
#     search_fields = ['text', ]
#     ordering_fields = ['created_at', ]
#     permission_classes = (IsAuthenticated, IsOwnerOrAdmin)
#     serializer_class = CommentCreateSerializer,


class UpdateComment(generics.UpdateAPIView):
    queryset = Comment.objects.filter(is_deleted=False).prefetch_related("author")
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_fields = ["author", "model_type", "model_id", "created_at", "updated_at"]
    search_fields = ['text', ]
    ordering_fields = ['created_at', ]
    permission_classes = (IsAuthenticated, IsOwnerOrAdmin)
    serializer_class = CommentUpdateSerializer,

# class DestroyComment(generics.DestroyAPIView):
#     queryset = Comment.objects.filter(is_deleted=False).prefetch_related("author")
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
#     filterset_fields = ["author", "model_type", "model_id", "created_at", "updated_at"]
#     search_fields = ['text', ]
#     ordering_fields = ['created_at', ]
#     permission_classes = (IsAuthenticated, IsOwnerOrAdmin)
#     serializer_class = CommentListSerializer,
