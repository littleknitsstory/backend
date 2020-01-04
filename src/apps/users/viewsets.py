from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.users.models import User
from .serializer import UserSerializer


class UserAPIViewSet(ReadOnlyModelViewSet):
    """ User viewset """
    queryset = User.objects.all()
    serializer_class = UserSerializer
