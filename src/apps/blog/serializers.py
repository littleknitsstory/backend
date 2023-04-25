from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.apps.blog.models import Article
from src.apps.blog.models import Tag

User = get_user_model()


class AuthorArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "avatar",
            "first_name",
            "last_name",
        )


class TagsForArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "title",
            "slug",
        )


class ArticleListSerializer(serializers.ModelSerializer):
    tags = TagsForArticleSerializer(many=True, read_only=True)
    image_preview = serializers.CharField(source="get_image")
    author = AuthorArticleSerializer(read_only=True)

    class Meta:
        model = Article
        fields = (
            "title",
            "slug",
            "content",
            "author",
            "tags",
            "image_preview",
            "image_alt",
            "created_at",
        )


class ArticleRetrieveSerializer(serializers.ModelSerializer):
    tags = TagsForArticleSerializer(many=True, read_only=True)
    image_preview = serializers.CharField(source="get_image")
    author = AuthorArticleSerializer(read_only=True)

    class Meta:
        model = Article
        fields = (
            "title",
            "slug",
            "content",
            "is_active",
            "author",
            "tags",
            "image_preview",
            "image_alt",
            "meta_title",
            "meta_keywords",
            "meta_description",
            "created_at",
            "updated_at",
        )
