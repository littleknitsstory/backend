from django.db import models

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from src.apps.reactions.choices import ReactionAssociationChoices
from src.core.mixins.mixin import SeoMixin


class Reaction(SeoMixin):
    """Reaction model"""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="reactions",
        on_delete=models.CASCADE,
        verbose_name=_("Author"),
    )
    text = models.CharField(_("Text"), max_length=263)
    model_type: ReactionAssociationChoices = models.CharField(
        _("Model type"),
        choices=ReactionAssociationChoices.MODEL_CHOICES,
        blank=True,
        default=ReactionAssociationChoices.REACTION,
        max_length=20
    )
    model_id = models.IntegerField(_("Associated"), blank=True, default=0)
    is_deleted = models.BooleanField(_("Deleted"), default=False)

    def __str__(self):
        return f"#{self.pk} by {self.author}"

    class Meta:
        verbose_name = _("Reaction")
        verbose_name_plural = _("Reactions")

