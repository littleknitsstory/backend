from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from src.apps.comments.models import Comment
from src.apps.comments.serializers import CommentListSerializer, CommentRetrieveSerializer


class CommentList(ModelViewSet):
    queryset = Comment.objects.filter(is_deleted=False)
    http_method_names = ["get", "post", "put", "patch"]

    serializer_classes = {
        "list": CommentListSerializer,
        "retrieve": CommentRetrieveSerializer,
    }
    filterset_fields = ["author", "to_model", "model_id", "created_at", "updated_at"]
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, CommentListSerializer)
