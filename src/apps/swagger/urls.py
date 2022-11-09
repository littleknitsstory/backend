from django.urls import re_path

from src.apps.swagger.views import schema_view

urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=None),
        name="schema-json",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=None),
        name="schema-redoc",
    ),
    re_path(
        r"^$",
        schema_view.with_ui("swagger", cache_timeout=None),
        name="schema-swagger-ui",
    ),
]
