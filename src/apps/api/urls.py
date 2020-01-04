from django.urls import include, path

urlpatterns = [
    path('', include('src.apps.blog.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', include('apps.shop.urls')),
    # path('', include('apps.menu.routes')),
    # path('', include('apps.slider.routes')),
    # path('', include('apps.tags.routes')),
    # path('', include('apps.contacts.routes')),
    # path('', include('apps.users.routes'))
]

