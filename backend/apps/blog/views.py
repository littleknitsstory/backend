from django.views.generic import DetailView, ListView, View
from django.shortcuts import render
from .models import Article
from apps.contacts.forms.subscribe import SubscribeForm
from django.conf import settings
from django.contrib.auth.models import User


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

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['more_posts'] = Article.objects.all().order_by('?')[:3]
        context['next_previews'] = Article.objects.all().exclude(title=context['object']).order_by('?')[:2]
        return context


class AuthorListView(ListView):
    model = Article
    template_name = 'blog/list.html'
    paginate_by = settings.PAGINATION_BY

    def get_queryset(self, **kwargs):
        author = User.objects.get(username=self.kwargs['author'])
        queryset = Article.objects.filter(author=author.id)
        return queryset


def error_404(request):  # FIXME почему это тут?
    return render(request, 'httpresponse/404.html', status=404)  # noqa
