from django.core.validators import EmailValidator
from rest_framework import serializers

from src.apps.contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])

    class Meta:
        model = Contact
        fields = (
            'name',
            'message',
            'phone_number',
            'email',
            'company',
        )
