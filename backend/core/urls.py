from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers

from apps.blog.views import ArticleList

router = routers.DefaultRouter()
router.register(r'posts', ArticleList)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include('apps.blog.urls')),
    path('shop/', include('apps.shop.urls')),
    path('subscribe/', include('apps.subscribe.urls', namespace='subscribe')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls

# http://www.django-rest-framework.org/api-guide/routers/#usage
