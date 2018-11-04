from django.urls import path

from .views import ProductListView, ProductDetailView, ProductsListView

urlpatterns = [
    path('categories/<slug:slug>/', ProductsListView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view()),
]
