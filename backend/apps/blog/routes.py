from rest_framework import routers
from .viewsets import ArticleList

urlpatterns = []

router_posts = routers.DefaultRouter()
router_posts.register(r'posts', ArticleList)

urlpatterns += router_posts.urls