from rest_framework import routers
from .viewsets import MenuAPIViewSet


urlpatterns = []

router_menu = routers.DefaultRouter()
router_menu.register(r'menu', MenuAPIViewSet)

urlpatterns += router_menu.urls
