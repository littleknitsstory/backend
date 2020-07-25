from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from src.apps.shorter.viewsets import UrlShorterViewset

router = routers.DefaultRouter()
router.register(r"shorteners", UrlShorterViewset, basename="shorteners")


urlpatterns = [
    path("", include(router.urls)),
    # path('l/<slug:slug>/', views.redirector_view),
]

# urlpatterns = [
#     path('<str:url_short>/', UrlShorterViewset.as_view(), name='url_short'),
# ]
