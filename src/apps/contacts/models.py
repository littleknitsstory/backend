from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=63, null=True, blank=True)
    message = models.TextField(_("Message"))
    phone_number = models.CharField(
        _("Phone number"), max_length=13, null=True, blank=True
    )
    email = models.EmailField(_("Email"))
    company = models.CharField(_("Company"), max_length=63, null=True, blank=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.message[:25]
