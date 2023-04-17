from django.urls import path, include
from rest_framework import routers

# TODO: change name of Pattern (viewsets)
from src.apps.patterns.viewsets import PatternViewset

app_name = "patterns"

router = routers.DefaultRouter()
router.register(r"patterns", PatternViewset)

urlpatterns = [
    path("", include(router.urls)),
]