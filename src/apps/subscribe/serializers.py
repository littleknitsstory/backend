from rest_framework import serializers

from src.apps.subscribe.models import Subscribe


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('email', )
        
    def validate_email(self):
        pass
