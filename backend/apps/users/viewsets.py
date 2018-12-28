from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializer import UserSerializer
from .models import User


class UserAPIViewSet(ReadOnlyModelViewSet):
    """ User viewset """
    queryset = User.objects.all()
    serializer_class = UserSerializer
