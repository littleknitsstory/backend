from django.urls import path
from .views import menu_index


urlpatterns = [
    path('', menu_index, name='index')
]
