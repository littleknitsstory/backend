from decouple import config

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.apps.feature_flags.models import Feature
from src.apps.feature_flags.serializers import FeatureSerializer


class FeatureViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = FeatureSerializer
    lookup_field = "name"
    permission_classes = [AllowAny]
    pagination_class = None

    def get_queryset(self):
        q_s = Feature.objects.all()
        for feature in q_s:
            flag = config("FEATURE_FLAG_" + feature.name.upper(), "").capitalize()
            if flag in ("True", "False"):
                feature.is_active = {"True": True, "False": False}[flag]
        return q_s

    def list(self, request, *args, **kwargs):
        flags = {f.name: f.is_active for f in self.get_queryset()}
        return Response(data=flags, content_type="application/json", status=200)
