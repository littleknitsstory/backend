from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.ListView.as_view(), name='review-list'),
    path('/add_review/', views.add_review, name='add-review')
]