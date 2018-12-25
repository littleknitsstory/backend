from django.urls import path
from apps.users.views import ProfileView
from rest_framework import routers
from .viewsets import UserAPIViewSet


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
]

router_user = routers.DefaultRouter()
router_user.register(r'user', UserAPIViewSet)

urlpatterns += router_user.urls
