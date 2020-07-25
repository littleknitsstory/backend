from math import ceil
from uuid import uuid4

from django.utils.translation import gettext_lazy as _
from django.db import models


def generate_token(length):
    return "".join([uuid4().hex for _ in range(ceil(length / 32))])[:length]


class UrlShorter(models.Model):
    url = models.URLField(_("Url"), max_length=1024)
    url_short = models.CharField(max_length=6, unique=True)
    count = models.IntegerField(default=0)
    is_expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True)
    update_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name = "Short Link"
        verbose_name_plural = "Short Links"
        ordering = ('-created_at',)
        
    def save(self):
        pass
