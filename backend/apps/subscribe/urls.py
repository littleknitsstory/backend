from django.urls import path
from .views import ViewSubscribe

urlpatterns = [
    path('', ViewSubscribe.as_view(), name='subscribe')
]
