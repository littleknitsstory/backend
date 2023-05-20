from django.urls import path, include
from rest_framework import routers

from src.apps.patterns.viewsets import ChatCompletionViewSet
from src.apps.patterns.viewsets import PatternViewset

app_name = "patterns"


router = routers.DefaultRouter()
router.register(r"patterns", PatternViewset)
router.register(
    r"patterns/generate_pdf/(?P<uuid>[^/.]+)",
    ChatCompletionViewSet,
    basename="generate_pdf",
)


urlpatterns = [
    path("", include(router.urls)),
]
