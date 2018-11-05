from django.urls import path

from .views import UserLoginView, UserRegisterView

urlpatterns = [
    path('', UserLoginView.as_view()),
    path('autors/login', UserLoginView.as_view()),
    path('autors/register', UserRegisterView.as_view()),
]
