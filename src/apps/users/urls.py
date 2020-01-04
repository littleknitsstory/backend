from django.urls import path, include
from rest_framework import routers
from .viewsets import UserAPIViewSet


router_user = routers.DefaultRouter()
router_user.register(r'user', UserAPIViewSet)

urlpatterns = [
    path('', include(router_user.urls)),
]
