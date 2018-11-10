from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from apps.blog.models import Article
from .models import Tag


class TagsList(ListView):
    def get(self, request, slug):
        context = {}
        tags = get_object_or_404(Tag, slug=slug)
        context['object_list'] = Article.objects.filter(tags=tags)
        return render(request, 'blog/list.html', context)



