from django.urls import path, include
from rest_framework import routers

from src.apps.account.viewsets import UserViewSet

router_user = routers.DefaultRouter()
router_user.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router_user.urls)),
]
