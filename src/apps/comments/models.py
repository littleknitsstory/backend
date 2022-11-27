from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from src.apps.comments.choices import CommentAssociationChoices
from src.core.mixins.mixin import SeoMixin


class Comment(SeoMixin):
    """Comment model"""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name=_("Author"),
    )
    text = models.CharField(_("Text"), max_length=263)
    model_type: CommentAssociationChoices = models.CharField(
        _("Model type"),
        choices=CommentAssociationChoices.MODEL_CHOICES,
        blank=True,
        default=CommentAssociationChoices.COMMENT,
        max_length=20
    )
    model_id = models.IntegerField(_("Associated"), blank=True, default=0)
    is_deleted = models.BooleanField(_("Deleted"), default=False)

    def __str__(self):
        return f"#{self.pk} by {self.author}"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
