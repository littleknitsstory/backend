from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Article
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Article
    template_name = 'blog/list.html'
    paginate_by = settings.PAGINATION_BY

    def get_queryset(self, **kwargs):
        queryset = super(BlogListView, self).get_queryset(**kwargs)
        try:
            if self.kwargs['author']:
                author = User.objects.get(username=self.kwargs['author'])
                queryset = Article.objects.filter(author=author.id)
                return queryset
        except KeyError:
            return queryset

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['crumb_title'] = 'Блог'
        context['crumb_url'] = reverse_lazy('blog:blog-list')
        return context


class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['crumb_title'] = 'Блог'
        context['crumb_url'] = reverse_lazy('blog:blog-list')
        context['more_posts'] = Article.objects.all().order_by('?')[:3]
        object_post = context['object']
        last_post = Article.objects.latest('id')
        # FIXME: поправить вывод крайних постов
        if object_post.id == 1:
            context['next_preview'] = Article.objects.get(id=2)
        elif object_post.id == last_post.id:
            context['previous_preview'] = Article.objects.get(id=(last_post.id - 1))
        else:
            context['next_preview'] = Article.objects.get(id=(object_post.id + 1))
            context['previous_preview'] = Article.objects.get(id=(object_post.id - 1))
        return context


def error_404(request):  # FIXME почему это тут?
    return render(request, 'httpresponse/404.html', status=404)  # noqa
