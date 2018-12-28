from rest_framework import routers
from .viewsets import SliderAPIViewSet


urlpatterns = []

router_slider = routers.DefaultRouter()
router_slider.register(r'slider', SliderAPIViewSet)

urlpatterns += router_slider.urls
