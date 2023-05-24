from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.apps.blog.models.bookmark import Bookmark
from src.apps.blog.models.models import Article, ArticleContent, Tag

User = get_user_model()

READING_SYMBOL_IN_SECOND = 17


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


class ArticleContentSerializer(serializers.ModelSerializer):
    image_alt = serializers.CharField()

    class Meta:
        model = ArticleContent
        fields = (
            "text",
            "image",
            "image_alt",
        )


class ArticleListSerializer(serializers.ModelSerializer):
    tags = TagsForArticleSerializer(many=True, read_only=True)
    contents = ArticleContentSerializer(many=True, read_only=True)
    # image_preview = serializers.CharField(source="get_image")
    author = AuthorArticleSerializer(read_only=True)

    class Meta:
        model = Article
        fields = (
            "title",
            "slug",
            "contents",
            "author",
            "tags",
            "created_at",
        )


class ArticleRetrieveSerializer(serializers.ModelSerializer):
    tags = TagsForArticleSerializer(many=True, read_only=True)
    contents = ArticleContentSerializer(many=True, read_only=True)
    author = AuthorArticleSerializer(read_only=True)
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (
            "title",
            "slug",
            "contents",
            "is_active",
            "author",
            "tags",
            "meta_title",
            "meta_keywords",
            "meta_description",
            "created_at",
            "updated_at",
            "is_bookmarked",
        )

    def get_is_bookmarked(self, article):
        user = self.context["request"].user
        if user.is_authenticated:
            is_bookmarked = Bookmark.objects.filter(user=user, article=article).exists()
            return is_bookmarked
        return False

    def to_representation(self, instance):
        data = super(ArticleRetrieveSerializer, self).to_representation(instance)
        data.update(
            {"time_for_read": len(instance.content) // READING_SYMBOL_IN_SECOND}
        )
        return data


class BookmarkSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    article = serializers.SlugRelatedField(
        slug_field="slug", queryset=Article.objects.all()
    )

    class Meta:
        model = Bookmark
        fields = ["id", "user", "article"]
        read_only_fields = ["id"]
