from rest_framework import serializers
from .models import Tag


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
            'slug',
            'title_seo',
            'meta_keywords',
            'meta_description',
            'created_at',
            'update_at'
        )