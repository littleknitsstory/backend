from rest_framework import routers
from .viewsets import DeliveryView

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'delivery'


urlpatterns = [
    path('mail-delivery', DeliveryView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

