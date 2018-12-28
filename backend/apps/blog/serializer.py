from rest_framework import serializers
from apps.tags.serializer import TagsSerializer
from apps.users.serializer import UserSerializer
from apps.blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    author = UserSerializer()
    tags = TagsSerializer(many=True, read_only=True)

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
