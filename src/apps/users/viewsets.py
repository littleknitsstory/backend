from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenViewBase

from src.apps.users.permissions import IsOwner
from src.apps.users.serializers import (
    SignUpSerializer,
    SignInSerializer,
    SignOutSerializer,
    UsersSerializer,
)

User = get_user_model()


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
        return Response(status=200)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ["get", "put"]
    serializer_class = UsersSerializer
    pagination_class = None

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.filter(username=self.request.user.username)
        return self.queryset

    def get_permissions(self):
        if self.action in [
            "retrieve",
            "list",
        ]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwner()]
        return []
