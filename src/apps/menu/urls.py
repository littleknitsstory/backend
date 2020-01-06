from django.urls import path, include
from rest_framework import routers
from .viewsets import MenuAPIViewSet

menu = routers.DefaultRouter()
menu.register(r'menu', MenuAPIViewSet)

urlpatterns = [
	path('', include(menu.urls))
]
