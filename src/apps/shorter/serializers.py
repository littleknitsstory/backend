from rest_framework import serializers


import logging

from src.apps.shorter.models import UrlShorter

logger = logging.getLogger(__name__)


class UrlShorterSerializer(serializers.ModelSerializer):
    url = serializers.URLField(required=False)
    url_short = serializers.URLField(required=False)

    class Meta:
        model = UrlShorter
        fields = "__all__"

    def create(self, validated_data):
        print("validated_data")
        print(validated_data)
        d = {"url": "https://google2.com", "url_short": "https://google2.com"}

        return d
