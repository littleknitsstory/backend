from django.utils.translation import gettext_lazy as _


class ReactionAssociationChoices:
    ARTICLE = "ARTICLE"
    COMMENT = "COMMENT"

    MODEL_CHOICES = (
        (ARTICLE, _("Article")),
        (COMMENT, _("Comment")),
    )
