from rest_framework import serializers

from src.apps.shop.models.product import ProductPhoto
from src.apps.shop.models import (
    Product,
    Category,
    OrderCartItem,
    OrderCart,
    ProductColor,
)


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            "title",
            "slug",
            "title_seo",
            "meta_keywords",
            "meta_description",
            "products",
        )

    def get_products(self, obj):
        products = Product.objects.filter(categories=obj, is_active=True)
        return ProductListSerializer(products, many=True).data


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "title",
            "slug",
        )


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ("color",)


class ProductPhotoSerializer(serializers.ModelSerializer):
    image_preview = serializers.CharField(source='get_image')

    class Meta:
        model = ProductPhoto
        fields = ("image_preview", "image_alt")


class ProductRetrieveSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True, read_only=True)
    colors = ColorSerializer(read_only=True, many=True)
    photo_product = ProductPhotoSerializer(many=True, read_only=True)
    image_preview = serializers.CharField(source='get_image')
    price = serializers.CharField(source='get_price')
    sale = serializers.CharField(source='get_sale')

    class Meta:
        model = Product
        fields = (
            "id",
            "code",
            "title",
            "slug",
            "description",
            "price",
            "price_currency",
            "sale",
            "sale_currency",
            "categories",
            "author",
            "count",
            "type_product",
            "material",
            "included",
            "height",
            "weight",
            "colors",
            "photo_product",
            # ImagesMixin
            "image_preview",
            "image_alt",
            # SeoMixin
            "title_seo",
            "meta_keywords",
            "meta_description",
            "created_at",
            "update_at",
        )


class ProductListSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True, read_only=True)
    colors = ColorSerializer(read_only=True, many=True)
    image_preview = serializers.CharField(source='get_image')
    price = serializers.CharField(source='get_price')
    sale = serializers.CharField(source='get_sale')

    class Meta:
        model = Product
        fields = (
            "id",
            "code",
            "title",
            "slug",
            "description",
            "price",
            "sale",
            "colors",
            "categories",
            "author",
            "image_preview",
            "image_alt",
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCartItem
        fields = ("pk", "product", "amount")


class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)

    class Meta:
        model = OrderCart
        fields = (
            "pk",
            "products",
            "phone",
            "address",
            "comments",
        )

    def create(self, validated_data):
        products_data = validated_data.pop("products")
        order = OrderCart.objects.create(**validated_data)
        for product_data in products_data:
            OrderCartItem.objects.create(**product_data)
        return order
