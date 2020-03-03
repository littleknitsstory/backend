from django.urls import path, include
from rest_framework import routers

from src.apps.reviews.viewsets import ReviewViewSet

router = routers.DefaultRouter()
router.register(r"reviews", ReviewViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
