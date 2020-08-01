from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.views import TokenViewBase

from src.apps.account.choices import AccountTypeChoices
from src.apps.account.serializers import (
    UserSerializer,
    SignUpSerializer,
    SignInSerializer,
    SignOutSerializer,
    ProfileSerializer,
    ConfirmSerializer,
)
from src.apps.account.models import User


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(account_type=AccountTypeChoices.AUTHOR)
    serializer_class = UserSerializer
    pagination_class = None
    lookup_field = "username"
    permission_classes = (AllowAny,)


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)


class SignInView(TokenViewBase):
    serializer_class = SignInSerializer
    permission_classes = (AllowAny,)


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


class ConfirmView(generics.RetrieveAPIView):
    serializer_class = ConfirmSerializer
    http_method_names = ["get"]

    def get_object(self):
        print(dir(self.request))
        print(self.request.user)
        print(self.request.content_type)
        print(self.request.data)
        print(self.request.parser_context)
        return self.request.query_params
