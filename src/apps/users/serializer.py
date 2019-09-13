from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            # 'jwt_secret',
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
