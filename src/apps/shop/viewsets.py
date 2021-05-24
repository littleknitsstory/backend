from rest_framework import status, mixins
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from src.apps.shop.models.order import OrderCart, OrderCartItem
from src.apps.shop.serializers import (
    OrderSerializer,
    OrderItemSerializer,
    CategoryRetrieveSerializer,
    CategoryListSerializer,
    ProductListSerializer,
    ProductRetrieveSerializer,
    OrderRetrieveSerializer,
)
from src.apps.shop.models import Product, Category


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True).prefetch_related("categories")
    lookup_field = "slug"
    http_method_names = ["get"]

    serializer_classes = {
        "list": ProductListSerializer,
        "retrieve": ProductRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, ProductListSerializer)


class CategoryViewSet(ModelViewSet):
    """Category for products"""

    queryset = Category.objects.all()
    http_method_names = ["get"]
    lookup_field = "slug"
    pagination_class = None
    serializer_classes = {
        "list": CategoryListSerializer,
        "retrieve": CategoryRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, CategoryListSerializer)


class OrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """Viewsets order
    ```
    {
        "products":  [{"product": int, "amount": int}, {"product": int, "amount": int}],
        "prices": int,
        "name": "str",
        "phone": "str",
        "address": "str",
        "comments": "str"
    }
    ```

    """

    permission_classes = (AllowAny,)
    queryset = OrderCart.objects.all()
    http_method_names = ["post", "get"]
    lookup_field = "order_number"
    serializer_classes = {
        "retrieve": OrderRetrieveSerializer,
        "create": OrderSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, OrderSerializer)


class OrderItemViewSet(ModelViewSet):
    """Viewsets order items"""

    permission_classes = (AllowAny,)
    serializer_class = OrderItemSerializer
    queryset = OrderCartItem.objects.all()
    http_method_names = ["post"]
