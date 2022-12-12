from django.urls import path, include
from rest_framework import routers

from src.apps.comments.viewsets import CommentList

app_name = "comments"

router = routers.DefaultRouter()
router.register(r"comments", CommentList)

urlpatterns = [
    path("", include(router.urls)),
]
