from rest_framework import routers
from .viewsets import TagsAPIViewSet


urlpatterns = []

router_tags = routers.DefaultRouter()
router_tags.register(r'tag', TagsAPIViewSet)

urlpatterns += router_tags.urls