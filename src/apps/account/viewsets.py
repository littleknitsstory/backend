from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework_simplejwt.views import TokenViewBase

from src.apps.account.choices import AccountTypeChoices
from src.apps.account.models import User
from src.apps.account.serializers import (
    UserSerializer,
    SignUpSerializer,
    SignInSerializer,
    SignOutSerializer,
    ProfileSerializer,
    ConfirmSerializer,
)


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


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self) -> User:
        return self.request.user


class ProfileViewSet(ModelViewSet):

    queryset = User.objects.all()
    http_method_names = ["get"]
    # lookup_field = "slug"
    pagination_class = None
    serializer_classes = {}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, ProfileSerializer)



class ConfirmView(generics.GenericAPIView):
    serializer_class = ConfirmSerializer
    
    def get(self, request):
        # TODO: add in dashboard
        # email = request.query_params.get("email")
        # code = request.query_params.get("code")
        # print(f"")
        return Response(status=status.HTTP_200_OK)
