from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializer import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAPIViewSet(ReadOnlyModelViewSet):
    """ User viewset """
    queryset = User.objects.all()
    serializer_class = UserSerializer
