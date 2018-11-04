import os
from django.conf import settings
from decouple import config


# DATABASES = {
#     'default': {
#         'ENGINE': '',
#         'NAME': config('POSTGRES_USER'),
#         'USER': config('POSTGRES_USER'),
#         'PASSWORD': config('POSTGRES_USER'),
#         'HOST': config('POSTGRES_USER'),
#         'PORT': config('POSTGRES_USER'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}
