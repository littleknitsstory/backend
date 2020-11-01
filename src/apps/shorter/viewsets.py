from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from src.apps.shorter.serializers import UrlShorterSerializer
from src.apps.shorter.models import UrlShorter


class UrlShorterViewset(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UrlShorterSerializer
    queryset = UrlShorter.objects.all()
    http_method_names = ["post", "get"]
    pagination_class = None
    lookup_field = "url_short"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.count += 1
        instance.save()
        return HttpResponseRedirect(instance.url)

    # serializer_classes = {
    #     "retrieve": UrlShorterSerializer,
    #     # "list": UrlShorterRetrieveSerializer,
    #     "create": UrlShorterSerializer,
    # }
    #
    # def get_serializer_class(self):
    #     return self.serializer_classes.get(self.action, UrlShorterSerializer)

    def list_2(self, url_short):
        short_link = get_object_or_404(UrlShorter, url_short=url_short)
        short_link.count += 1
        short_link.save()
        return HttpResponseRedirect(short_link.url)
