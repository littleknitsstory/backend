from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.apps.blog.models.models import Article
from .models.bookmark import Bookmark
from .serializers import (
    ArticleListSerializer,
    ArticleRetrieveSerializer,
    BookmarkSerializer,
)


class ArticleList(ModelViewSet):
    queryset = Article.objects.filter(is_active=True).prefetch_related("tags")
    http_method_names = ["get"]
    lookup_field = "slug"

    serializer_classes = {
        "list": ArticleListSerializer,
        "retrieve": ArticleRetrieveSerializer,
    }
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, ArticleListSerializer)


class BookmarkList(ArticleList):
    http_method_names = ["get", "post", "delete"]
    serializer_classes = {
        "create": BookmarkSerializer,
        "destroy": BookmarkSerializer,
    }
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=["post"])
    def add_bookmark(self, request, slug=None):
        article = self.get_object()
        if Bookmark.objects.filter(user=request.user, article=article).exists():
            return Response(
                {"errors": "The article is already bookmarked"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        bookmark = Bookmark.objects.create(user=request.user, article=article)
        serializer = BookmarkSerializer(bookmark)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["delete"])
    def delete_bookmark(self, request, slug=None):
        article = self.get_object()
        try:
            bookmark = Bookmark.objects.get(user=request.user, article=article)
        except Bookmark.DoesNotExist:
            return Response(
                {"errors": "The article is not bookmarked by the user"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        bookmark.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
