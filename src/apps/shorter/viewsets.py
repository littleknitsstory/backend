from django.http import HttpResponseRedirect
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from src.apps.shorter.models import UrlShorter
from src.apps.shorter.serializers import UrlShorterSerializer


class UrlShorterViewset(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UrlShorterSerializer
    queryset = UrlShorter.objects.all()
    http_method_names = ["get"]
    pagination_class = None
    lookup_field = "url_short"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.count += 1
        instance.save()
        return HttpResponseRedirect(instance.url)
