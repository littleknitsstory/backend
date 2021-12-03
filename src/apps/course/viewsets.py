from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.account.models import User


class CoursesViewSet(ModelViewSet):
    queryset = User.objects.none()
    # serializer_class =
    # http_method_names = ["get"]
    permission_classes = (AllowAny,)
