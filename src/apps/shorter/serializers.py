from rest_framework import serializers


import logging

from src.apps.shorter.models import UrlShorter

logger = logging.getLogger(__name__)


class UrlShorterSerializer(serializers.ModelSerializer):
    url = serializers.URLField(required=False)
    url_short = serializers.URLField(required=False, source="get_url_short")

    class Meta:
        model = UrlShorter
        fields = ("url", "url_short")
