from django.forms import ModelForm, Textarea

from apps.contacts.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'email', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }
