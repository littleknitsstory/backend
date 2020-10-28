from django.urls import path, include
from rest_framework import routers

from src.apps.blog.viewsets import ArticleList

app_name = "blog"

router = routers.DefaultRouter()
router.register(r"posts", ArticleList)

urlpatterns = [
    path("", include(router.urls)),
]
