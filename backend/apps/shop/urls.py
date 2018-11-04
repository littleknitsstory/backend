from django.urls import path

from .views import ProductListView, ProductDetailView, CategoryProductsListView

urlpatterns = [
    path('categories/<slug:slug>/', CategoryProductsListView.as_view()),
    path('', ProductListView.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view()),
]
