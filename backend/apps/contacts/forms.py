from django.utils.translation import ugettext_lazy as _

from captcha.fields import CaptchaField
from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    fields = ['name', 'email', 'feedback', 'captcha']
    captcha = CaptchaField()

    class Meta:
        model = Contact
