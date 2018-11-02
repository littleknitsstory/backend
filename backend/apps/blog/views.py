from django.views.generic import DetailView, TemplateView
from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleSerializer

# ModelViewSet ListAPIView
class ArticleList(ModelViewSet):
    queryset = Article.objects.prefetch_related('tags').all()
    serializer_class = ArticleSerializer


class ListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('?')[:4]
        return context


class DetailView(DetailView):
    model = Article
    template_name = 'detail.html'
