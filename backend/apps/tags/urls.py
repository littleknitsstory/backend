from django.urls import path
from .views import TagsList
from rest_framework import routers
from .viewsets import TagsAPIViewSet

app_name = 'tags'

urlpatterns = [
    path('<slug:slug>/', TagsList.as_view(), name='tags-list'),

    ]

router_tags = routers.DefaultRouter()
router_tags.register(r'tag', TagsAPIViewSet)

urlpatterns += router_tags.urls
