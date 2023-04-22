from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import PatternSerializer
from .models import Pattern


class PatternViewset(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Pattern.objects.all()
    http_method_names = ["post", "get"]
    lookup_field = "uuid"
    serializer_classes = {
        "create": PatternSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, PatternSerializer)
