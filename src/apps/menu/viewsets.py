from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import MenuItemsSerializer
from .models import MenuItems


class MenuAPIViewSet(ReadOnlyModelViewSet):
    queryset = MenuItems.objects.filter(is_active=True)
    serializer_class = MenuItemsSerializer
