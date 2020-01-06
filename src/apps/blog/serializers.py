from rest_framework import serializers

from src.apps.blog.models import Tag
from src.apps.blog.models import Article


class TagsForArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'title',
            'slug',
        )


class ArticleListSerializer(serializers.ModelSerializer):
    tags = TagsForArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            'title',
            'slug',
            'content',
            'author',
            'tags',
            'image_preview',
            'image_alt',
            'created_at',
        )


class ArticleRetrieveSerializer(serializers.ModelSerializer):
    tags = TagsForArticleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = (
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
