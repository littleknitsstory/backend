from rest_framework import serializers
from src.apps.patterns.models import Pattern


class PatternSerializer(serializers.ModelSerializer):
    prompt = serializers.CharField()

    class Meta:
        model = Pattern
        fields = (
            "pattern_number",
            "prompt",
            "created_up",
            #"author",
        )

class PatternUpdateSerializer(serializers.ModelSerializer):
    pass
#
#     raw_pattern = serializers.JSONField()
#
#     def update(self, instance, validated_data):
#         pass
#
    class Meta:
        model = Pattern
        fields = '__all__'
    #     fields = (
    #         "pattern_number",
    #         "prompt",
    #         "raw_pattern"
    #         "created_up",
    #         "update_up"
    #         "author",
    #     )