from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", "POSTGRES_DB"),
        "USER": config("POSTGRES_USER", "POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD", "POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST", "localhost"),
        "PORT": config("POSTGRES_PORT", 5432),
    }
}
