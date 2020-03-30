import sentry_sdk
from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=config("SENTRY_DNS", ""), integrations=[DjangoIntegration()],
)
