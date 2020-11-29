import logging
from typing import Union, List

from django.conf import settings
from django.core.mail import get_connection, send_mail

from src.core.celery import app

logger = logging.getLogger(__name__)


def _get_connection(backend: str):
    if backend:
        backend, api_key = (
            settings.ANYMAIL.get(f"{backend}_EMAIL_BACKEND"),
            settings.ANYMAIL.get(f"{backend}_API_KEY"),
        )
        return get_connection(backend=backend, api_key=api_key)


# TODO: use it? @app.task(time_limit=10, soft_time_limit=8)
@app.task()
def send_email_celery(
    subject: str,
    to: List[str],
    message: str,
    from_email: str = None,
    html_message: str = None,
    backend: str = settings.PROVIDER_EMAIL,
) -> Union[bool, Exception]:
    from_email = settings.EMAIL_HOST_USER if from_email is None else from_email

    try:
        connection = _get_connection(backend=backend)
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=to,
            fail_silently=False,
            auth_user=None,
            auth_password=None,
            connection=connection,
            html_message=html_message,
        )
        logger.info(f"Send message successfully to {to}, subject - {subject}")
        return True

    except Exception as e:
        logger.error(f"Not send mail with Celery to {to}, - {e}, subject - {subject}")
        return e
