from django.urls import path, include
from rest_framework import routers

from src.apps.patterns.viewsets import PatternViewset


app_name = "patterns"


router = routers.DefaultRouter()
router.register(r"patterns", PatternViewset)


urlpatterns = [
    path("", include(router.urls)),
]
