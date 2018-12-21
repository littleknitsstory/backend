from django.forms import ModelForm, EmailInput
from apps.contacts.models import Subscribe
from django.core.exceptions import ValidationError


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']

        widgets = {
            'email': EmailInput(attrs={'class': 'form-control b-subcribe_form__input', 'id': 'email-data', 'placeholder': 'Адрес почты'})
        }

    def clean(self):
        cleaned_data = super(SubscribeForm, self).clean()
        email_exists = Subscribe.objects.filter(email=cleaned_data['email'])
        if email_exists:
            raise ValidationError('Вы уже подписаны!')
