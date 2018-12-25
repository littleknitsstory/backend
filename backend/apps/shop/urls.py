from django.urls import path
from rest_framework import routers
from .viewsets import ProductAPIViewSet, CategoryAPIViewSet
from .views import ProductListView, ProductDetailView, \
    CategoryProductsListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductDashboardView

app_name = 'shop'

# https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers
urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('dashboard/', ProductDashboardView.as_view(), name='dashboard'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<slug:slug>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<slug:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/<slug:slug>/', CategoryProductsListView.as_view(), name='category'),
]

router_product = routers.DefaultRouter()
router_product.register(r'product', ProductAPIViewSet)
router_category = routers.DefaultRouter()
router_category.register(r'category', CategoryAPIViewSet)

urlpatterns += router_product.urls
urlpatterns += router_category.urls

