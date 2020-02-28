from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.apps.shop.models.order import OrderCart, OrderCartItem
from src.apps.shop.serializers import OrderSerializer, OrderItemSerializer, \
    CategoryRetrieveSerializer, CategoryListSerializer, ProductListSerializer, ProductRetrieveSerializer
from src.apps.shop.models import Product, Category


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True).prefetch_related('categories')
    lookup_field = 'slug'
    http_method_names = ['get']

    serializer_classes = {
        'list': ProductListSerializer,
        'retrieve': ProductRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, ProductListSerializer)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(ModelViewSet):
    """Category for products"""
    queryset = Category.objects.all()
    http_method_names = ['get']
    lookup_field = 'slug'
    pagination_class = None
    serializer_classes = {
        'list': CategoryListSerializer,
        'retrieve': CategoryRetrieveSerializer,
    }
    
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, CategoryListSerializer)


class OrderViewSet(ModelViewSet):
    """ Viewsets order
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
    serializer_class = OrderSerializer
    queryset = OrderCart.objects.all()
    http_method_names = ['post']


class OrderItemViewSet(ModelViewSet):
    """ Viewsets order items """
    permission_classes = (AllowAny,)
    serializer_class = OrderItemSerializer
    queryset = OrderCartItem.objects.all()
    http_method_names = ['post']
