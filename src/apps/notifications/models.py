import email
import uuid
import os
from pathlib import Path


from django.db import models
#from django.core.mail import send_mail as send_email_celery
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from jinja2 import Environment, FileSystemLoader

from src.settings.components import _paths, redis
from src.core.utils.send_mail import logger, send_email_celery

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'core\\utils')
TEMPLATE_FILE = 'sidnup.html'


class Templates(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    path = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_template(slug: str) -> object or False:
        try:
            #template = Templates.objects.get(slug=slug)
            env = Environment(loader=FileSystemLoader(BASE_DIR))
            template = env.get_template(TEMPLATE_FILE)
        except Templates.DoesNotExist:
            logger.warning(f'template is not found')
            return False
        except Exception as e:
            logger.warning(f'{e}. Something went wrong with slug... {slug}, get_template()')
            return False
        html_str = template.render()
        return html_str

    def _get_context(self) -> dict:
        return {
            'TITLE': self.title,
            'SUBJECT': self.subject,
            'TEXT': self.text,
            'UNSUBSCRIBE_TEXT': _(
                'The letter has been sent to the specified mail'
            ),
            'static': _paths.STATIC_ROOT,
        }

    def get_html_template(self) -> str:
        return render_to_string(
            template_name=self.get_template(),
            context=self._get_context()
        )


class SendMail(models.Model):

    def set_code(email):
        key = str(uuid.uuid4()).replace("-", "")
        redis.REDIS_CONNECT.set(email, key, ex=300)
        return key

    def send_confirm(self):
        # TODO: need templates for welcome mail
        code = self.set_code(self.email.lower())
        message = f"dev.backend.littleknitsstory.com:26363/api/v1/confirm/?code={code}"
        send_email_celery.delay(to=[self.email], subject=_("Welcome"), message=message)
