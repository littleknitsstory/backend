from django.urls import path, include
from .views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),

    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/author/<author>/', BlogListView.as_view(), name='author-list'),
]
