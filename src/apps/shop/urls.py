from django.urls import path, include
from rest_framework import routers

from src.apps.shop.viewsets import ProductViewSet, CategoryViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = [
    path("", include(router.urls)),
]
