from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializer import ArticleSerializer
from .models import Article
from rest_framework.response import Response
from django.http import Http404


class ArticleList(ModelViewSet):
    queryset = Article.objects.prefetch_related('tags').all()
    serializer_class = ArticleSerializer


class ArticleAPICRUD(APIView):
    queryset = Article.objects.all()

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ArticleSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ArticleSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
