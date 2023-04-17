from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from src.apps.users.viewsets import (
    SignUpView,
    SignInView,
    SignOutView,
    #    ConfirmView,
    UsersViewSet,
)

router_user = routers.DefaultRouter()
router_user.register(r"users", UsersViewSet, basename="users")


urlpatterns = [
    path("", include(router_user.urls)),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("sign-in/", SignInView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("sign-out/", SignOutView.as_view(), name="logout"),
    # path("confirm/", ConfirmView.as_view(), name="confirm"),
]
