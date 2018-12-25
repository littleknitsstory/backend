from rest_framework import routers
from apps.contacts.viewsets import ContactAPIViewSet


urlpatterns = [

]

router_contact = routers.DefaultRouter()
router_contact.register(r'contact', ContactAPIViewSet)

urlpatterns += router_contact.urls