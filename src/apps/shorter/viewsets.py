from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from src.apps.shorter.serializers import UrlShorterSerializer
from src.apps.shorter.models import UrlShorter


class UrlShorterViewset(ModelViewSet):
    
    permission_classes = (AllowAny,)
    # serializer_class = UrlShorterSerializer
    queryset = UrlShorter.objects.all()
    http_method_names = ["post", "get"]
    pagination_class = None
    serializer_classes = {
        # "retrieve": UrlShorterRetrieveSerializer,
        # "list": UrlShorterRetrieveSerializer,
        "create": UrlShorterSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, UrlShorterSerializer)
    
    def get_object(self):
        return self.request.query_params


class UrlShorterRedirectViewset(View):

    def get(self, request, url_short):
        short_link = get_object_or_404(UrlShorter, url_short=url_short)
        short_link.count += 1
        short_link.save()
        return HttpResponseRedirect(short_link.url)
