from django.urls import path, include
from rest_framework import routers
from .viewsets import ProductViewSet, CategoryViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'quick_orders', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
