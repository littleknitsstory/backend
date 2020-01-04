from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'account_type',
            'username',
            'avatar',
            'phone_number',
            'country',
            'city',
            'birth_date',
            'email',
            'is_email_confirmed',
            'is_profile_full',
            'vk_profile',
            'fb_profile'
        )
