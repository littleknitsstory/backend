from django.views.generic import DetailView, TemplateView
from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleSerializer
from apps.subscribe.forms import SubscribeForm


class ArticleList(ModelViewSet):
    queryset = Article.objects.prefetch_related('tags').all()
    serializer_class = ArticleSerializer


class BlogListView(TemplateView):
    template_name = 'blog/list.html'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('?')[:4]
        context['form_subscribe'] = SubscribeForm()
        return context


class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
