from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title="Shop API")

urlpatterns = [
    path("", include("src.apps.swagger.urls")),
    path("api/v1/", include("src.apps.api.urls")),
    path("admin/", admin.site.urls),
    path("anymail/", include("anymail.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("api/v2/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # path('i18n/', include('django.conf.urls.i18n')),
    # path("auth/", include("rest_framework_social_oauth2.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += [
#     path('google5e682b3d95e1b8ef.html',
#     TemplateView.as_view(template_name='google-auth.html')),
#     path('yandex_5486c91ec180b084.html',
#     TemplateView.as_view(template_name='yandex-auth.html')),
# ]

# http://www.django-rest-framework.org/api-guide/routers/#usage
