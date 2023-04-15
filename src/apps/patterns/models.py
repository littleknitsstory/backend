from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import ShortUUIDField


class Pattern(models.Model):
    pattern_number = ShortUUIDField(_("Pattern number"))
    prompt = models.TextField('Users text')
    #raw_pattern = models.JSONField('gpt response')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="pattern_user",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Author"),
    )
    created_up = models.DateTimeField('request time', auto_now_add=True)
    #update_up = models.DateTimeField('request update', default=None)
