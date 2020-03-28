from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.apps.reviews.models import Review
from src.apps.reviews.serializers import ReviewSerializer


class ReviewViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Review.objects.filter(is_active=True)[:2]
    serializer_class = ReviewSerializer
    http_method_names = ["get"]
    pagination_class = None
