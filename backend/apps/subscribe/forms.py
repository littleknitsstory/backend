from django.forms import ModelForm, EmailInput
from .models import Subscribe


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control b-subcribe_form__input'})
        }
