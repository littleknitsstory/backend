from django.urls import path

from .views import ProductListView, ProductDetailView, \
    CategoryProductsListView, ProductCreateView

app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('products/create/', ProductCreateView.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/<slug:slug>/', CategoryProductsListView.as_view(), name='category'),
]
