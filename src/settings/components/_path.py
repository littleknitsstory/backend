ROOT_URLCONF = "src.core.urls"
WSGI_APPLICATION = "src.core.wsgi.application"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # src/
ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)  # root/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, "media")
