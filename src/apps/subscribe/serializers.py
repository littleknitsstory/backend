from django.core.validators import EmailValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


from src.apps.subscribe.models import Subscribe


class SubscribeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    
    class Meta:
        model = Subscribe
        fields = ('email', )
        
    def validate_email(self, obj):
        if Subscribe.objects.filter(email=obj).exists():
            raise ValidationError(_('Email is exists'))
        return obj

