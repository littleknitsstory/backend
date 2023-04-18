from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    # определяем поле для ключа content
    content = serializers.CharField()


class ChoicesSerializer(serializers.Serializer):
    # определяем поле для ключа message с вложенным сериализатором
    message = MessageSerializer()


class DataSerializer(serializers.Serializer):
    # определяем поле для ключа choices с вложенным сериализатором
    choices = ChoicesSerializer(many=True)
