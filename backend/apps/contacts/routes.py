from rest_framework import routers
from apps.contacts.viewsets import ContactAPIViewSet
from apps.contacts.viewsets import FeedbackAPIViewSet
from apps.contacts.viewsets import ReviewAPIViewSet


urlpatterns = []

router_contact = routers.DefaultRouter()
router_contact.register(r'contact', ContactAPIViewSet)

router_feedback = routers.DefaultRouter()
router_feedback.register(r'feedback', FeedbackAPIViewSet)

router_reviews = routers.DefaultRouter()
router_reviews.register(r'reviews', ReviewAPIViewSet)

urlpatterns += router_reviews.urls
urlpatterns += router_feedback.urls
urlpatterns += router_contact.urls
