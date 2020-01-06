from django.urls import path, include
from rest_framework import routers
from .viewsets import SliderAPIViewSet

router_slider = routers.DefaultRouter()
router_slider.register(r'sliders', SliderAPIViewSet)

urlpatterns = [
    path('', include(router_slider.urls)),
]
