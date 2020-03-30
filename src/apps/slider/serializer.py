from rest_framework import serializers
from .models import Slider


class SliderSerializer(serializers.ModelSerializer):
    image_preview = serializers.CharField(source="get_image")

    class Meta:
        model = Slider
        fields = (
            "title",
            "slug",
            "sub_title",
            "ordering",
            "link",
            "image_preview",
            "image_alt",
        )
