from django.urls import path
from .views import BlogListView, BlogDetailView, AjaxBlogListView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('blog/moreposts/', AjaxBlogListView.as_view()),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/author/<author>/', BlogListView.as_view(), name='author-list'),
]
