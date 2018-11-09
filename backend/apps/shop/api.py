from rest_framework.viewsets import ModelViewSet

from .serialazer import ProductSerializer
from .models import Product


class ProductAPIViewSet(ModelViewSet):
    queryset = Product.objects.prefetch_related('category', 'tags').all()
    serializer_class = ProductSerializer
