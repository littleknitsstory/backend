import uuid

from django.db import models
from django.core.mail import send_mail as send_email_celery
from django.shortcuts import render

from src.core.utils import send_mail


class Templates(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.TextField()
    slug = models.SlugField(unique=True)

    def get_template(self, slug):
        return render('src/core/signup.html')


class SendMail(models.Model):

    def set_code(email):
        key = str(uuid.uuid4()).replace("-", "")
        # settings.REDIS_CONNECT.set(email, key, ex=300)
        return key


    def send_confirm(self):
        # TODO: need templates for welcome mail
        code = self.set_code(self.email.lower())
        message = f"dev.backend.littleknitsstory.com:26363/api/v1/confirm/?code={code}"
        send_email_celery.delay(to=[self.email], subject=_("Welcome"), message=message)
