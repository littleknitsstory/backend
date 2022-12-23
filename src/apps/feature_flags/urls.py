from django.urls import path, include
from rest_framework import routers

from src.apps.feature_flags.viewsets import FeatureViewSet

router = routers.DefaultRouter()
router.register(r"features", FeatureViewSet, basename="features")

urlpatterns = [
    path("", include(router.urls)),
]
