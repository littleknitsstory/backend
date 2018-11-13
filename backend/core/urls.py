from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers

from apps.blog.views import ArticleList
from apps.shop.api import ProductAPIViewSet


router = routers.DefaultRouter()
router.register(r'api/posts', ArticleList)
router.register(r'api/shop', ProductAPIViewSet)

urlpatterns = [
    path('', include('apps.blog.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('captcha/', include('captcha.urls')),
    path('social/', include('social_django.urls', namespace='social')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('shop/', include('apps.shop.urls', namespace='shop')),
    path('subscribe/', include('apps.subscribe.urls', namespace='subscribe')),
    path('tags/', include('apps.tags.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls

# urlpatterns += [
#     path('google5e682b3d95e1b8ef.html', TemplateView.as_view(template_name='google-auth.html')),
#     path('yandex_5486c91ec180b084.html', TemplateView.as_view(template_name='yandex-auth.html')),
# ]

# http://www.django-rest-framework.org/api-guide/routers/#usage
