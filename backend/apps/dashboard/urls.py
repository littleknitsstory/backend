from django.urls import path

from apps.dashboard.views import DashboardListView

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardListView.as_view(), name='list'),
    # path('<pk:pk>/list', DashboardListView.as_view(), name='list'),
]
