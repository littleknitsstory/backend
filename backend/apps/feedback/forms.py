from django.forms import ModelForm

from .models import Feedback


class FeedbackForm(ModelForm):
    fields = ['name', 'email', 'feedback', 'captcha']
    # captcha = CaptchaField()

    class Meta:
        model = Feedback
