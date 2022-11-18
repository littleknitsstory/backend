import logging

import sentry_sdk
#from decouple import config
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR,
)

# Sentry ON for production
#if config("ENVIRONMENT", "test") == "production":
#    sentry_sdk.init(
#        dsn=config("SENTRY_DNS", ""),
#        integrations=[DjangoIntegration(), sentry_logging],
#    )
