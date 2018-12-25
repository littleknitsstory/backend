from django.urls import path
from .views import TagsList


app_name = 'tags'

urlpatterns = [
    path('<slug:slug>/', TagsList.as_view(), name='tags-list'),

    ]

