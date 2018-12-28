from rest_framework.viewsets import ModelViewSet
from .serializer import ArticleSerializer
from .models import Article


class ArticleList(ModelViewSet):
    """ Posts viewset """
    queryset = Article.objects.prefetch_related('tags').all()
    serializer_class = ArticleSerializer


