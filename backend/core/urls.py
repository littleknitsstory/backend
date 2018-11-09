from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers

from apps.blog.views import ArticleList
from apps.shop.api import ProductAPIViewSet


router = routers.DefaultRouter()
router.register(r'posts', ArticleList)
router.register(r'api/shop', ProductAPIViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', include('apps.blog.urls')),
    path('subscribe/', include('apps.subscribe.urls')),
    path('shop/', include('apps.shop.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls

# http://www.django-rest-framework.org/api-guide/routers/#usage
