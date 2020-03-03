import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://e396c654fac2472f8fd2117e49ca1164@sentry.io/1474916",
    integrations=[DjangoIntegration()],
)
