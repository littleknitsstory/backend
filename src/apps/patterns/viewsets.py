from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import PatternSerializer, PatternUpdateSerializer
from .models import Pattern


class PatternViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Pattern.objects.all()
    http_method_names = ["post", "get", "put"]
    lookup_field = "pattern_number"
    serializer_classes = {
        "create": PatternSerializer,
        'update': PatternUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, PatternSerializer)
