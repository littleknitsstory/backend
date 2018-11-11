from django.urls import path

from .views import ContactCreateView

app_name = 'contacts'

urlpatterns = [
    path('', ContactCreateView.as_view(), name='contact_create'),
]
