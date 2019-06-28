from rest_framework import routers
from .viewsets import DeliveryView

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'delivery'


urlpatterns = [
    path('pochta', DeliveryView.as_view()) #/<from_city>/<from_street>/<to_city>/<to_street>
]

urlpatterns = format_suffix_patterns(urlpatterns)

