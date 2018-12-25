from django.urls import path
from apps.contacts.views.feedback import FeedbackCreateView
from rest_framework import routers
from apps.contacts.viewsets import FeedbackAPIViewSet

app_name = 'feedback'

urlpatterns = [
    path('', FeedbackCreateView.as_view(), name='contact_create'),
]

router_feedback = routers.DefaultRouter()
router_feedback.register(r'feedback', FeedbackAPIViewSet)

urlpatterns += router_feedback.urls
