from django.urls import path, include
from rest_framework import routers

from src.apps.contacts.viewsets import ContactsViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
