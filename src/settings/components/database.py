#from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lks_db',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}

#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.postgresql_psycopg2",
#        "NAME": config("POSTGRES_DB", "POSTGRES_DB"),
#        "USER": config("POSTGRES_USER", "POSTGRES_USER"),
#        "PASSWORD": config("POSTGRES_PASSWORD", "POSTGRES_PASSWORD"),
#        "HOST": config("POSTGRES_HOST", "postgresql"),
#        "PORT": config("POSTGRES_PORT", 5432),
#    }
#}
