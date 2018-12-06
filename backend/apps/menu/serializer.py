from rest_framework import serializers

from apps.menu.models import MenuItems


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = '__all__'

