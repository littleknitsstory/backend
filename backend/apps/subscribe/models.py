from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscribe(models.Model):
    email =  models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    hidden = models.CharField(max_length=200)

    class Meta:
        verbose_name = _('Subscribe')
        verbose_name_plural = _('Subscribers')

    def __str__(self):
        return self.email
