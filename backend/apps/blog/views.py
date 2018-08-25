from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleSerializer


# ModelViewSet ListAPIView
class ArticleList(ModelViewSet):
    queryset = Article.objects.prefetch_related('tags').all()
    serializer_class = ArticleSerializer


