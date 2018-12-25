from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializer import ContactSerializer, ReviewSerializer, FeedbackSerializer
from .models import Contact, Review, Feedback


class ContactAPIViewSet(ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ReviewAPIViewSet(ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class FeedbackAPIViewSet(ReadOnlyModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
