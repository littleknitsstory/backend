from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=120)
    slug = AutoSlugField(_("slug"), populate_from="title", editable=True)

    meta_title = models.CharField(_("Title Seo"), max_length=500, blank=True, null=True)
    meta_keywords = models.TextField(_("Keywords"), blank=True, null=True)
    meta_description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title
