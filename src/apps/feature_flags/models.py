from django.db import models
from django.utils.translation import gettext_lazy as _

class Feature(models.Model):
    name = models.CharField(_("Title"), max_length=24, blank=True)
    is_active = models.BooleanField(_("Active"), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")
