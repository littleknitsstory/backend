from rest_framework import serializers

from src.apps.feature_flags.models import Feature


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ("name", "is_active", )
        read_only_fields = ("name", )
