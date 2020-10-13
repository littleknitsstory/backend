from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        license=openapi.License(name="BSD License"),
        contact=openapi.Contact(email="support@littleknitsstory.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
