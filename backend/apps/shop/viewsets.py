from rest_framework.viewsets import ModelViewSet
from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductAPIViewSet(ModelViewSet):
    """ Shop product viewset """
    queryset = Product.objects.prefetch_related('category', 'tags').all()
    serializer_class = ProductSerializer
    # ModelViewSet уже дает весь КРУД


class CategoryAPIViewSet(ModelViewSet):
    """ Shop category viewset """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



