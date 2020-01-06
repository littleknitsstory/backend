from rest_framework import serializers

from src.apps.account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'avatar',
            'about',
            'vk_profile',
            'fb_profile',
            'inst_profile',
            'tg_profile',
        )
