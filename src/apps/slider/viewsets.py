from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from .serializer import SliderSerializer
from .models import Slider


class SliderAPIViewSet(mixins.ListModelMixin, GenericViewSet):
    """Slider viewset"""

    queryset = Slider.objects.filter(is_active=True)
    serializer_class = SliderSerializer
    pagination_class = None
    permission_classes = (AllowAny,)
