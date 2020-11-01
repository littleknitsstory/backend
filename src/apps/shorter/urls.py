from django.urls import path, include
from rest_framework import routers

from src.apps.shorter.viewsets import UrlShorterViewset

router = routers.DefaultRouter()
router.register(r"l", UrlShorterViewset, basename="shorteners")


urlpatterns = [
    path("", include(router.urls)),
]
