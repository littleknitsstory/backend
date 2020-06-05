from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from src.apps.shop.models.product import ProductPhoto
from src.apps.shop.models import (
    Product,
    Category,
    OrderCartItem,
    OrderCart,
    ProductColor,
)

import logging

logger = logging.getLogger(__name__)


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
    image_preview = serializers.CharField(source="get_image")

    class Meta:
        model = ProductPhoto
        fields = ("image_preview", "image_alt")


class ProductRetrieveSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True, read_only=True)
    colors = ColorSerializer(read_only=True, many=True)
    photo_product = ProductPhotoSerializer(many=True, read_only=True)
    image_preview = serializers.CharField(source="get_image")
    price = serializers.CharField(source="get_price")
    sale = serializers.CharField(source="get_sale")

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
    image_preview = serializers.CharField(source="get_image")
    price = serializers.CharField(source="get_price")
    sale = serializers.CharField(source="get_sale")

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
        fields = ("pk", "order_cart", "product", "amount")


class OrderSerializer(serializers.Serializer):
    products = OrderItemSerializer(many=True)
    phone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    comments = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    def validate_products(self, products):
        products_count = len(products)
        products_ids = []
        for product in products:
            products_ids.append(product.get("product").id)
            product_count = product.get("product")
            product_count = product_count.count
            amount = product.get("amount", 0)
            if amount > product_count:
                logger.info(f"Product {product} less than requested {amount}")
                raise ValidationError(_("Product less than requested"))
        if products_count != len(set(products_ids)):
            raise ValidationError(_("The order contains a duplicate of the goods"))
        return products

    # FIXME: order.save() in def save()
    def create(self, validated_data):
        products_data = validated_data.pop("products")
        order = OrderCart.objects.create(**validated_data)
        for product_data in products_data:
            order_item = OrderCartItem.objects.create(**product_data)
            order_item.order_cart = order
            order_item.item_total_cost = order_item.get_total_cost_item()
            order_item.save()
        order.order_total_cost = order.get_total_cost_order()
        order.save()
        return order


class OrderRetrieveSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)

    class Meta:
        model = OrderCart
        fields = (
            "products",
            "order_number",
            "status",
        )
