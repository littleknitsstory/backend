from rest_framework import routers
from .viewsets import ProductAPIViewSet, CategoryAPIViewSet

urlpatterns = []

router_product = routers.DefaultRouter()
router_product.register(r'product', ProductAPIViewSet)
router_category = routers.DefaultRouter()
router_category.register(r'category', CategoryAPIViewSet)

urlpatterns += router_product.urls
urlpatterns += router_category.urls