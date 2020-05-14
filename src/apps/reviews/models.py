from django.utils.translation import gettext_lazy as _
from django.db import models

from src.core.mixins.mixin import ImagesMixin


class Review(ImagesMixin):
    title = models.CharField(_("Title"), max_length=63)
    author = models.CharField(_("Author review"), max_length=63)
    comment = models.CharField(_("Comment"), max_length=263)
    email = models.EmailField(_("Email"), blank=True, null=True)
    rating = models.PositiveSmallIntegerField(_("Rating"))
    is_active = models.BooleanField(_("Active"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        ordering = ("-created_at",)

    def __str__(self):
        return self.author
