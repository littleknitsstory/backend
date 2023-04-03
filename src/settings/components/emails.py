from decouple import config

EMAIL_HOST = config("EMAIL_HOST", "")
EMAIL_PORT = config("EMAIL_PORT", "")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", "")
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = config(
    "EMAIL_HOST_USER", "noreply@mg.littleknitsstory.com"
)

PROVIDER_EMAIL = config("PROVIDER_EMAIL", "MAILGUN")  # MAILGUN, SENDGRID
