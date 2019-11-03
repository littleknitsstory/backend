from django.views import View

from django.contrib.auth import authenticate, get_user_model, login
from django.urls import reverse_lazy
from django_registration import signals
from django_registration.views import RegistrationView
from django_registration.forms import RegistrationForm
# from src.core.utils.send_mail import SendEmail
from django.contrib.auth import get_user_model
User = get_user_model()


class ProfileView(View):
    pass


class RegistrationViews(RegistrationView):

    form_class = RegistrationForm
    success_url = reverse_lazy('django-registration-complete')

    def register(self, form):
        new_user = form.save()
        new_user = authenticate(**{
            User.USERNAME_FIELD: new_user.get_username(),
            'password': form.cleaned_data['password1']
        })
        login(self.request, new_user)
        signals.user_registered.send(
            sender=self.__class__,
            user=new_user,
            request=self.request
        )
        from_email = 'admin@lks.ru'
        to_email = form.cleaned_data['email']
        subject = 'Спасибо за регистрацию'
        content = '<div style="color: grey;"><h1>Hello</h1></div>'
        # mail = SendEmail(from_email, to_email, subject, content)
        # mail.send()
        return new_user
