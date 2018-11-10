from django.urls import path

from apps.users.views import UserLoginView

urlpatterns = [
    path('', UserLoginView.as_view()),
]
