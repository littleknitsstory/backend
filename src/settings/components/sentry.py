from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration
import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

# All of this is already happening by default!
sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR,  # Send errors as events
)

sentry_sdk.init(
    dsn=config("SENTRY_DNS", ""),
    integrations=[DjangoIntegration(), sentry_logging],
)
