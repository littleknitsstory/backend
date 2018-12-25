from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializer import MenuItemsSerializer
from .models import MenuItems


class MenuAPIViewSet(ReadOnlyModelViewSet):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

