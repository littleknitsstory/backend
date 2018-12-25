from django.urls import path
from apps.contacts.views.feedback import FeedbackCreateView


app_name = 'feedback'

urlpatterns = [
    path('', FeedbackCreateView.as_view(), name='contact_create'),
]

