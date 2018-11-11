from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
]
