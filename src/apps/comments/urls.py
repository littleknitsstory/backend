from django.urls import path, include
from rest_framework import routers

from src.apps.comments.viewsets import CommentList, UpdateComment

app_name = "comments"

# router = routers.DefaultRouter()
# router.register("comments", CommentList.as_view())

urlpatterns = [
   # path("", include(router.urls)),
    path("comments", CommentList.as_view()),
    path("comments/<int:pk>/", UpdateComment.as_view()),
   # path("comments", CommentList.as_view()),
]
