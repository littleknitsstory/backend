from django.views.generic import ListView, DetailView

from .models.category import Category
from .models.product import Product


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['host'] = self.request.META['wsgi.url_scheme'] \
                          + '://' + self.request.META['HTTP_HOST']
        return context


class CategoryProductsListView(ListView):
    model = Category
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
        context['host'] = self.request.META['wsgi.url_scheme'] \
                          + '://' + self.request.META['HTTP_HOST']
        return context

