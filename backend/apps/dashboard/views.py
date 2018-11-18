from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView

from apps.blog.models import Article
from apps.shop.models import Product


class DashboardListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/list.html'
    context_object_name = 'object'

    def get_queryset(self):
        queryset = super(DashboardListView, self).get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        context['products'] = Product.objects.all()

        return context
