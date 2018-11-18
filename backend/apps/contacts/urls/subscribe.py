from django.urls import path
from apps.contacts.views import AjaxSubscribe, SuccessSubscribe

app_name = 'subscribe'

urlpatterns = [
    path('ajax/', AjaxSubscribe.as_view(), name='ajax_subscribe'),
    path('success/', SuccessSubscribe.as_view(), name='success_subscribe'),
]
