from django.urls import path
from .views import BlogListView, BlogDetailView
from rest_framework import routers
from .viewsets import ArticleList

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/author/<author>/', BlogListView.as_view(), name='author-list'),
]

router_posts = routers.DefaultRouter()
router_posts.register(r'posts', ArticleList)

urlpatterns += router_posts.urls
