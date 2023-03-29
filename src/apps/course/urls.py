from django.urls import path, include
from rest_framework import routers

from src.apps.course.viewsets import CoursesViewSet

router = routers.DefaultRouter()
router.register(r"courses", CoursesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
