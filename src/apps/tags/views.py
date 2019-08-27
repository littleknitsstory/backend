from django.views.generic import ListView
from apps.blog.models import Article
from .models import Tag
from django.conf import settings


class TagsList(ListView):
    model = Tag
    template_name = 'blog/list.html'
    paginate_by = settings.PAGINATION_BY

    def get_queryset(self, **kwargs):
        queryset = Article.objects.filter(tags__slug=self.kwargs['slug'])
        return queryset
