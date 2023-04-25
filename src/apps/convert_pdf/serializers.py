from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    content = serializers.CharField()


class ChoicesSerializer(serializers.Serializer):
    message = MessageSerializer()


class DataSerializer(serializers.Serializer):
    choices = ChoicesSerializer(many=True)
