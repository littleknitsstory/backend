from django.urls import path, include
from rest_framework import routers

from src.apps.reactions.viewsets import ReactionList

app_name = "reactions"

router = routers.DefaultRouter()
router.register(r"reactions", ReactionList)

urlpatterns = [
    path("", include(router.urls)),
]
