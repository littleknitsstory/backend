from django.views.generic import DetailView, ListView
from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleSerializer
from apps.subscribe.forms import SubscribeForm
from django.conf import settings


class ArticleList(ModelViewSet):
    queryset = Article.objects.prefetch_related('tags').all()
    serializer_class = ArticleSerializer


class BlogListView(ListView):
    model = Article
    template_name = 'blog/list.html'
    paginate_by = settings.PAGINATION_BY

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['form_subscribe'] = SubscribeForm()
        return context


class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
