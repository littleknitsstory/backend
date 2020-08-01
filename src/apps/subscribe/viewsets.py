from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from src.apps.subscribe.models import Subscribe
from src.apps.subscribe.serializers import SubscribeSerializer


class SubscribeViewSet(ModelViewSet):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.none()
    http_method_names = ["post"]
    permission_classes = (AllowAny,)
