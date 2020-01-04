from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.shop.models.order import OrderCart, OrderCartItem
from .serializer import ProductSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer
from .models import Product, Category


class ProductViewSet(ModelViewSet):
    """ Shop product viewset """
    queryset = Product.objects.prefetch_related('category').all()
    serializer_class = ProductSerializer
    # ModelViewSet уже дает весь КРУД


class CategoryViewSet(ModelViewSet):
    """ Shop category viewset """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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

