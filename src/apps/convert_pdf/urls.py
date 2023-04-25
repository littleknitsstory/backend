from django.urls import path, include
from rest_framework import routers

from src.apps.convert_pdf.viewsets import ChatCompletionViewSet

app_name = "convert_pdf"

router = routers.DefaultRouter()
router.register(r"convert_pdf", ChatCompletionViewSet, basename="convert_pdf")

urlpatterns = [
    path("", include(router.urls)),
]
