from django.urls import path
from apps.contacts.views.reviews import ReviewsListView, CreateReview


app_name = 'reviews'
urlpatterns = [
    path('', ReviewsListView.as_view(), name='review-list'),
    path('add_review/', CreateReview.as_view(), name='add-review')
]

