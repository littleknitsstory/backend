from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from apps.blog.models import Article
from .models import Tag
from django.conf import settings


class TagsList(ListView):
    model = Tag
    template_name = 'blog/list.html'
    paginate_by = settings.PAGINATION_BY

    def get_queryset(self, **kwargs):
        tags = get_object_or_404(Tag, slug=self.kwargs['slug'])
        queryset = Article.objects.filter(tags=tags)
        return queryset
