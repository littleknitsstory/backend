from rest_framework import routers
from apps.contacts.viewsets import ContactAPIViewSet, FeedbackAPIViewSet, ReviewAPIViewSet


urlpatterns = []

router = routers.DefaultRouter()
router.register(r'contact', ContactAPIViewSet)
router.register(r'feedback', FeedbackAPIViewSet)
router.register(r'reviews', ReviewAPIViewSet)

urlpatterns += router.urls
