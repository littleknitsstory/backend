from rest_framework import serializers

from apps.blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'title',
            'slug',
            'image_preview',
            'content',
            # 'category',
            # 'tags'
        )

        lookup_field = 'slug'
