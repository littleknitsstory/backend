from django.views import View

from django.contrib.auth import authenticate, get_user_model, login
from django.urls import reverse_lazy
from django_registration import signals
from django_registration.views import RegistrationView
from django_registration.forms import RegistrationForm
from .send_mail import SendEmail


class ProfileView(View):
    pass


User = get_user_model()


class RegistrationViews(RegistrationView):

    form_class = RegistrationForm
    success_url = reverse_lazy('django_registration_complete')

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
        mail = SendEmail('admin@lks.ru', form.cleaned_data['email'], 'Спасибо за регистрацию', 'Спасибо что зарегистрировались на нашем сайте!')
        mail.send()
        return new_user