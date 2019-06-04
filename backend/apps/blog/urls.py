from django.urls import path, include
from .views import BlogListView, BlogDetailView, AjaxBlogListView

from rest_framework import routers
from .viewsets import ArticleList

app_name = 'blog'

router = routers.DefaultRouter()
router.register(r'posts', ArticleList)


urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('blog/moreposts/', AjaxBlogListView.as_view()),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/author/<author>/', BlogListView.as_view(), name='author-list'),
]

urlpatterns += [
    # path('', include(router.urls)),

]
