from django.urls import path, include
from rest_framework import routers

from src.apps.blog.viewsets import ArticleList, BookmarkList

app_name = "blog"

router = routers.DefaultRouter()
router.register(r"articles", ArticleList)

urlpatterns = [
    path(
        "articles/<slug:slug>/bookmarks/",
        BookmarkList.as_view({"post": "add_bookmark", "delete": "delete_bookmark"}),
        name="article-add-bookmark",
    ),
    path("", include(router.urls)),
]
