from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscribe(models.Model):
    email = models.EmailField(verbose_name=_("Email"), blank=True, null=True)
    hidden = models.CharField(_("Hidden"), max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=_("created_at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")
