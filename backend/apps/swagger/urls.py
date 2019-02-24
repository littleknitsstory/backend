from django.conf.urls import url

from .views import schema_view

urlpatterns = [
   url(r'^swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=None),
       name='schema-json',
       ),
   url(r'^redoc/$',
       schema_view.with_ui('redoc', cache_timeout=None),
       name='schema-redoc',
       ),
   url(r'^$',
       schema_view.with_ui('swagger', cache_timeout=None),
       name='schema-swagger-ui',
       ),
]
