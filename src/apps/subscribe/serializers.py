from django.core.validators import EmailValidator
from rest_framework import serializers

from src.apps.subscribe.models import Subscribe


class SubscribeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    
    class Meta:
        model = Subscribe
        fields = ('email', )
        
    def validate_email(self, obj):
        pass
