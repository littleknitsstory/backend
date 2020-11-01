INSTALLED_APPS = [
    "modeltranslation",
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    # Plugins
    # Auth2
    # "oauth2_provider",
    # "social_django",
    # "rest_framework_social_oauth2",
    "anymail",
    "graphene_django",
    "corsheaders",
    "mptt",
    "ckeditor",
    "ckeditor_uploader",
    "optimized_image",
    "djmoney",
    "djmoney.contrib.exchange",
    "colorful",
    "robots",
    # Dev
    "django_extensions",
    # Django Rest Framework
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "drf_yasg2",
    # Apps project
    "src.apps.account",
    "src.apps.api",
    "src.apps.blog",
    "src.apps.contacts",
    "src.apps.menu",
    "src.apps.shop",
    "src.apps.shorter",
    "src.apps.slider",
    "src.apps.subscribe",
    "src.apps.reviews",
]

SITE_ID = 1
