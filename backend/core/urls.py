from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.blog.views import ArticleList

router = routers.DefaultRouter()
router.register(r'posts', ArticleList)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include('apps.blog.urls')),
    path('shop/', include('apps.shop.urls')),
    path('subscribe/', include('apps.subscribe.urls')),

]
urlpatterns += router.urls
# http://www.django-rest-framework.org/api-guide/routers/#usage
