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
            "updated_at",
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
    code = serializers.CharField(source="product.code", required=False)

    class Meta:
        model = OrderCartItem
        fields = ("product", "amount", "code")


class OrderSerializer(serializers.Serializer):
    products = OrderItemSerializer(many=True)
    phone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    comments = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    #
    status = serializers.CharField(required=False)
    order_number = serializers.CharField(required=False)

    def validate_products(self, products):
        products_count = len(products)
        products_ids = []
        for product in products:
            products_ids.append(product.get("product").id)
            product_count = product.get("product").count
            amount = product.get("amount", 0)
            if amount > product_count:
                logger.info(f"Product {product} less than requested {amount}")
                raise ValidationError(_("Product less than requested"))
        if products_count != len(set(products_ids)):
            raise ValidationError(_("The order contains a duplicate of the goods"))
        return products

    def create(self, validated_data):
        products_data = validated_data.pop("products")
        order = OrderCart.objects.create(**validated_data)
        bulk_inserts = []
        for product_data in products_data:
            bulk_inserts.append(OrderCartItem(order_cart=order, **product_data))
        item_data = OrderCartItem.objects.bulk_create(bulk_inserts)

        # item_data = OrderItemSerializer(item_data, many=True).data
        # need call save() bulk_create do *not* call save()
        order.save()

        return {
            "status": order.status,
            "order_number": order.order_number,
            "products": item_data,
        }


class OrderRetrieveSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)

    class Meta:
        model = OrderCart
        fields = (
            "products",
            "order_number",
            "status",
        )
