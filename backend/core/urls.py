from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from django.views.generic import TemplateView
import grappelli

from apps.blog.views import error_404
from apps.users.views import RegistrationViews


schema_view = get_swagger_view(title='Shop API')

urlpatterns = [
    path('', include('apps.blog.urls')),
    path('blog/comments/', include('fluent_comments.urls')), 
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegistrationViews.as_view(), name='django-registration-register'),
    path('accounts/register/complete/', TemplateView.as_view(
        template_name='django_registration/registration_complete.html'
    ), name='django-registration-complete'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('shop/', include('apps.shop.urls', namespace='shop')),
    path('tags/', include('apps.tags.urls')),
    path('subscribe/', include('apps.contacts.urls.subscribe', namespace='subscribe')),
    path('contacts/', include('apps.contacts.urls.feedback')),
    path('reviews/', include('apps.contacts.urls.reviews')),
    # libs
    path('pages/', include('django.contrib.flatpages.urls')),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('social/', include('social_django.urls', namespace='social')),

]

urls_api = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/docs/', schema_view),
    path('api/', include('apps.shop.routes')),
    path('api/', include('apps.blog.routes')),
    path('api/', include('apps.menu.routes')),
    path('api/', include('apps.slider.routes')),
    path('api/', include('apps.tags.routes')),
    path('api/', include('apps.contacts.routes')),
    path('api/', include('apps.users.routes'))
]

if settings.DEBUG:
    import debug_toolbar
    url_toolbar = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += url_toolbar
urlpatterns += urls_api
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = error_404

# urlpatterns += [
#     path('google5e682b3d95e1b8ef.html', TemplateView.as_view(template_name='google-auth.html')),
#     path('yandex_5486c91ec180b084.html', TemplateView.as_view(template_name='yandex-auth.html')),
# ]

# http://www.django-rest-framework.org/api-guide/routers/#usage
