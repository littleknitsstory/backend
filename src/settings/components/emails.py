from decouple import config

EMAIL_HOST = config("EMAIL_HOST", "")
EMAIL_PORT = config("EMAIL_PORT", "")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", "")
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = config(
    "EMAIL_HOST_USER", "noreply@mg.littleknitsstory.com"
)
# EMAIL_BACKEND


PROVIDER_EMAIL = config("PROVIDER_EMAIL", "MAILGUN")  # MAILGUN, SENDGRID

ANYMAIL = {
    "MAILGUN_API_KEY": config("MAILGUN_API_KEY", ""),
    "MAILGUN_API_URL": "https://api.mailgun.net/v3",
    "MAILGUN_SENDER_DOMAIN": "mg.littleknitsstory.com",
    "MAILGUN_EMAIL_BACKEND": "anymail.backends.mailgun.EmailBackend",
    "IGNORE_RECIPIENT_STATUS": True,
    # SENDGRID_EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
    # "SENDGRID_API_KEY": "",
    # "SENDGRID_API_URL": "",
    # "SENDGRID_SENDER_DOMAIN": "",
}
