from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView

from src.core.sitemap import sitemaps

urlpatterns = [
    # API's
    path("api/v1/", include("src.apps.api.urls")),
    path("api/v2/", csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
    # AUTH
    # path("auth/", include("rest_framework_social_oauth2.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # ADMIN
    path("nimda/", admin.site.urls),  # foolproof mirror url admin/
    path("ckeditor/", include("ckeditor_uploader.urls")),
    # SUPPORT
    path("docs/", include("src.apps.swagger.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("anymail/", include("anymail.urls")),
    path("_nested_admin/", include("nested_admin.urls")),
    # SEO
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt", include("robots.urls")),
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
