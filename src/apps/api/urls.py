from django.urls import include, path

urlpatterns = [
    path("", include("src.apps.blog.urls")),
    path("", include("src.apps.shop.urls")),
    path("", include("src.apps.menu.urls")),
    path("", include("src.apps.slider.urls")),
    path("", include("src.apps.account.urls")),
    path("", include("src.apps.subscribe.urls")),
    path("", include("src.apps.reviews.urls")),
    path("", include("src.apps.contacts.urls")),
    path("", include("src.apps.shorter.urls")),
    path("", include("src.apps.comments.urls")),
    path("", include("src.apps.feature_flags.urls")),
    path("", include("src.apps.reactions.urls")),
    path("", include("src.apps.convert_pdf.urls")),
]
