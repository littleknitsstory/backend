from rest_framework import serializers
from apps.tags.serializer import TagsSerializer

from apps.shop.models.order import OrderCartItem, OrderCart
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


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCartItem
        fields = ('pk', 'product', 'amount')


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)

    class Meta:
        model = OrderCart
        fields = ('pk', 'products', 'prices', 'name', 'phone', 'address', 'comments',)

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = OrderCart.objects.create(**validated_data)
        for product_data in products_data:
            OrderCartItem.objects.create(**product_data)
        return order
