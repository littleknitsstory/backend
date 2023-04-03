from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

from optimized_image.fields import OptimizedImageField


class Slider(models.Model):
    """Slider model"""

    title = models.CharField(_("Title"), max_length=120)
    slug = AutoSlugField(_("slug"), populate_from="title", editable=True)
    sub_title = models.CharField(_("Sub Title"), max_length=120, blank=True)
    is_active = models.BooleanField(_("Active"), default=True)
    ordering = models.IntegerField(_("Ordering"))
    link = models.URLField(_("Link"), blank=True)
    image_preview = OptimizedImageField(_("Images"), blank=True)
    image_alt = models.CharField(_("Images Alt"), blank=True, max_length=255)

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Sliders")
        ordering = ("ordering",)

    def __str__(self):
        return self.title

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(Slider, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )

    def get_image(self) -> str:
        try:
            image = self.image_preview.url
        except ValueError:
            image = None
        return image
