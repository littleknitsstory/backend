from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from src.apps.subscribe.models import Subscribe
from src.apps.subscribe.serializers import SubscribeSerializer


@permission_classes((AllowAny,))
class SubscribeViewSet(ModelViewSet):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.none()
    http_method_names = ['post']
