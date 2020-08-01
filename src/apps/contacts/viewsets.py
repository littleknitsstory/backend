from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


from src.apps.contacts.serializers import ContactSerializer
from src.apps.contacts.models import Contact


class ContactsViewSet(ModelViewSet):
    queryset = Contact.objects.none()
    serializer_class = ContactSerializer
    http_method_names = ["post"]
    permission_classes = (AllowAny,)
