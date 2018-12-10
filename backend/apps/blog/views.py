from django.views.generic import DetailView, ListView
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer
from apps.contacts.forms.subscribe import SubscribeForm
from django.conf import settings


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


def error_404(request, exception):
    return render(request, 'httpresponse/404.html', status=404)  # noqa
