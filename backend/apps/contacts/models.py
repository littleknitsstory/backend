from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    feedback = models.TextField()
    name = models.CharField(max_length=120)
    email = models.EmailField()

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.feedback[:25]
