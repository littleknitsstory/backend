from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenViewBase

from src.apps.account.choices import AccountTypeChoices
from src.apps.account.serializers import UserSerializer, SignUpSerializer, SignInSerializer, SignOutSerializer, \
    ProfileSerializer
from src.apps.account.models import User


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(account_type=AccountTypeChoices.AUTHOR)
    serializer_class = UserSerializer
    pagination_class = None
    lookup_field = 'username'


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer


class SignInView(TokenViewBase):
    serializer_class = SignInSerializer


class SignOutView(GenericAPIView):
    serializer_class = SignOutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self) -> User:
        return self.request.user
