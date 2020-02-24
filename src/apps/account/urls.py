from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from src.apps.account.viewsets import UserViewSet, SignUpView, SignInView, SignOutView, ProfileView

router_user = routers.DefaultRouter()
router_user.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router_user.urls)),
    path('sign-up/', SignUpView.as_view()),
    path('sign-in/', SignInView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sign-out/', SignOutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
