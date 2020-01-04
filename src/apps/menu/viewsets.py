from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializer import MenuItemsSerializer
from .models import MenuItems


class MenuAPIViewSet(ReadOnlyModelViewSet):
    """ Menu viewset """
    queryset = MenuItems.objects.filter(is_active=False)
    serializer_class = MenuItemsSerializer

