from django.urls import path, include
from src.apps.shop.viewsets import ProductViewSet, CategoryViewSet, OrderViewSet
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'quick_orders', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
