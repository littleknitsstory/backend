from rest_framework import routers
from .viewsets import ProductAPIViewSet, CategoryAPIViewSet

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'product', ProductAPIViewSet)
router.register(r'category', CategoryAPIViewSet)

urlpatterns += router.urls
