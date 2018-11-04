from django.forms import ModelForm, TextInput
from .models import Subscribe


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = {
            'email': TextInput(attrs={'class': 'form-control b-subcribe_form__input'})
        }
