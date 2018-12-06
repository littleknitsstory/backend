from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from apps.blog.views import ArticleList
from apps.shop.api import ProductAPIViewSet
from apps.menu.viewsets import MenuAPIViewSet
from apps.menu.viewsets import MenuAPICRUD

from apps.blog.views import error_404


router = routers.DefaultRouter()
router.register(r'api/posts', ArticleList)
router.register(r'api/shop', ProductAPIViewSet)
router.register(r'api/menu', MenuAPIViewSet)

schema_view = get_swagger_view(title='Shop API')

urlpatterns = [
    path('', include('apps.blog.urls')),
    path('api/docs/', schema_view),
    path('api/menu/<int:pk>/', MenuAPICRUD.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('captcha/', include('captcha.urls')),
    path('social/', include('social_django.urls', namespace='social')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('shop/', include('apps.shop.urls', namespace='shop')),
    path('tags/', include('apps.tags.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('subscribe/', include('apps.contacts.urls.subscribe', namespace='subscribe')),
    path('contacts/', include('apps.contacts.urls.feedback')),
    path('reviews/', include('apps.contacts.urls.reviews')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls


handler404 = error_404

# urlpatterns += [
#     path('google5e682b3d95e1b8ef.html', TemplateView.as_view(template_name='google-auth.html')),
#     path('yandex_5486c91ec180b084.html', TemplateView.as_view(template_name='yandex-auth.html')),
# ]

# http://www.django-rest-framework.org/api-guide/routers/#usage
