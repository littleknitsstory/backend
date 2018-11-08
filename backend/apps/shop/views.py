from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView

from .models.category import Category
from .models.product import Product

PAGINATION_BY = 6


class ProductListView(ListView):
    model = Product
    paginate_by = PAGINATION_BY
    template_name = 'shop/product_list.html'

    def get_queryset(self):
        return Product.objects.all().prefetch_related('category', 'tags')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context


class CategoryProductsListView(ListView):
    model = Category
    paginate_by = PAGINATION_BY
    template_name = 'shop/category_product_list.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(
            category__slug=self.kwargs['slug'], active=True
        ).prefetch_related('category', 'tags')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryProductsListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(
            slug=self.kwargs['slug']
        ).title
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    login_url = '/login/'
    fields = [
        'title', 'slug', 'image', 'image_alt', 'description',
        'keywords', 'price', 'active', 'category', 'tags'
    ]
    template_name = 'shop/product_form.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    login_url = '/login/'
    fields = [
        'title', 'slug', 'image', 'image_alt', 'description',
        'keywords', 'price', 'active', 'category', 'tags'
    ]
    template_name = 'shop/product_form.html'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('shop:main')
