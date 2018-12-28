from rest_framework import serializers

from apps.menu.models import MenuItems, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'id',
            'slug',
            'hint',
            'active'
        )


class MenuItemsSerializer(serializers.ModelSerializer):

    menu = MenuSerializer()

    class Meta:
        model = MenuItems
        fields = (
            'id',
            'name',
            'url',
            'menu',
            'target',
            'parent',
            'ordering',
            'active'
        )

