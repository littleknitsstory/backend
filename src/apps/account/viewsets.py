from rest_framework.viewsets import ReadOnlyModelViewSet

from src.apps.account.choices import AccountTypeChoices
from src.apps.account.serializers import UserSerializer
from src.apps.account.models import User


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(account_type=AccountTypeChoices.AUTHOR)
    serializer_class = UserSerializer
    pagination_class = None
    lookup_field = 'username'

