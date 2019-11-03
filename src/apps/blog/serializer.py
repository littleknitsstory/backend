from rest_framework import serializers

from src.apps.tags.models import Tag
# from src.apps.users.serializer import UserSerializer
from src.apps.blog.models import Article


class TagsForArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
            'slug',
        )


class ArticleSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    tags = TagsForArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'slug',
            'content',
            'is_active',
            'author',
            'tags',
            'image_preview',
            'image_alt',
            'title_seo',
            'meta_keywords',
            'meta_description',
            'created_at',
            'update_at'
        )
        lookup_field = 'slug'
