from django.urls import path
from apps.contacts.views.reviews import ReviewsListView, CreateReview
from rest_framework import routers
from apps.contacts.viewsets import ReviewAPIViewSet

app_name = 'reviews'
urlpatterns = [
    path('', ReviewsListView.as_view(), name='review-list'),
    path('add_review/', CreateReview.as_view(), name='add-review')
]

router_reviews = routers.DefaultRouter()
router_reviews.register(r'reviews', ReviewAPIViewSet)

urlpatterns += router_reviews.urls
