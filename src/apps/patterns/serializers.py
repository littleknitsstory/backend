from rest_framework import serializers

from src.apps.patterns.models import Pattern


class PatternSerializer(serializers.ModelSerializer):
    prompt = serializers.CharField()

    class Meta:
        model = Pattern
        fields = (
            "uuid",
            "prompt",
            "created_up",
        )
