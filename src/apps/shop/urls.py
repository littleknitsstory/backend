from django.urls import path, include
from src.apps.shop.viewsets import ProductViewSet, CategoryViewSet, OrderViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"categories", CategoryViewSet)
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"quick_orders", OrderViewSet, basename="quick_orders")


urlpatterns = [
    path("", include(router.urls)),
]
