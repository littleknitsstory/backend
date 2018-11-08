from django.urls import path

from .views import ProductListView, ProductDetailView, \
    CategoryProductsListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('products/create/', ProductCreateView.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<slug:slug>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<slug:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/<slug:slug>/', CategoryProductsListView.as_view(), name='category'),
]
