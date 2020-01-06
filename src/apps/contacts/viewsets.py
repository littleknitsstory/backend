from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ReviewSerializer, FeedbackSerializer
from .models import Review, Feedback


# class ContactAPIViewSet(ReadOnlyModelViewSet):
#     """ Contact viewset """
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer


class ReviewAPIViewSet(ReadOnlyModelViewSet):
    """ Review viewset """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class FeedbackAPIViewSet(ReadOnlyModelViewSet):
    """ Feedback viewset """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
