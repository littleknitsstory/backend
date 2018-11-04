from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

# from rest_framework import routers
# from apps.blog import urls

# router = routers.DefaultRouter()
# router.register(r'posts', views.ArticleList)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include('apps.blog.urls')),
    path('shop/', include('apps.shop.urls')),

# TODO MEDIA_URL is empty here - fix it!
] + static('/storage/media/', document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls
# http://www.django-rest-framework.org/api-guide/routers/#usage
