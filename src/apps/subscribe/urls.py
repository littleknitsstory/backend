from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from src.apps.subscribe.viewsets import SubscribeViewSet

router = DefaultRouter()
router.register(r'subscribe', SubscribeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
