from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from src.apps.shorter.serializers import UrlShorterSerializer
from src.apps.shorter.models import UrlShorter


class UrlShorterViewset(ModelViewSet):

    permission_classes = (AllowAny,)
    # serializer_class = UrlShorterSerializer
    queryset = UrlShorter.objects.all()
    http_method_names = ["post", "get"]
    pagination_class = None
    serializer_classes = {
        # "retrieve": UrlShorterRetrieveSerializer,
        # "list": UrlShorterRetrieveSerializer,
        "create": UrlShorterSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, UrlShorterSerializer)

    def get_object(self):
        return self.request.query_params
