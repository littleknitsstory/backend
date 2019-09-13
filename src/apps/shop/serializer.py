from rest_framework import serializers
from apps.tags.serializer import TagsSerializer
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'price',
            'sale',
            'is_active',
            'category',
            'tags',
            'author',
            # ImagesMixin
            'image_preview',
            'image_alt',
            # SeoMixin
            'title_seo',
            'meta_keywords',
            'meta_description',
            'created_at',
            'update_at'
        )
        lookup_field = 'slug'

        # Указать все явно поля
        # Поля со связями вывести полностью
        # ?read_only_fields = ('id', 'category_name')

