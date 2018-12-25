from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializer import SliderSerializer
from .models import Slider


class SliderAPIViewSet(ReadOnlyModelViewSet):
    """ Slider viewset """
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

