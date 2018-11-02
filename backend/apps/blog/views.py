from django.views import generic

from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleSerializer


# ModelViewSet ListAPIView
class ArticleList(ModelViewSet):
    queryset = Article.objects.prefetch_related('tags').all()
    serializer_class = ArticleSerializer


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('?')[:4]
        return context


class DetailView(generic.DetailView):
    model = Article
    template_name = 'detail.html'
