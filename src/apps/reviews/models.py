from django.utils.translation import gettext_lazy as _
from django.db import models

from optimized_image.fields import OptimizedImageField


class Review(models.Model):
    title = models.CharField(_("Title"), max_length=63)
    author = models.CharField(_("Author review"), max_length=63)
    comment = models.CharField(_("Comment"), max_length=263)
    email = models.EmailField(_("Email"), blank=True, null=True)
    rating = models.PositiveSmallIntegerField(_("Rating"))
    is_active = models.BooleanField(_("Active"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    image_preview = OptimizedImageField(_("Images"), blank=True)
    image_alt = models.CharField(_("Images Alt"), blank=True, max_length=255)

    def __str__(self):
        return self.author

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(Review, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )

    def get_image(self) -> str:
        try:
            image = self.image_preview.url
        except ValueError:
            image = None
        return image

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        ordering = ("-created_at",)
