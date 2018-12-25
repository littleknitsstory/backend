from rest_framework.viewsets import ModelViewSet
from .serializer import TagsSerializer
from .models import Tag


class TagsAPIViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
