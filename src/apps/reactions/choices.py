from django.utils.translation import gettext_lazy as _


class ReactionAssociationChoices:
    ARTICLE = "ARTICLE"
    COMMENT = "COMMENT"

    MODEL_CHOICES = (
        (ARTICLE, _("Article")),
        (COMMENT, _("Comment")),
    )

class ReactionChoices:
    RED_HEART = "RED_HEART"
    FIRE = "FIRE"
    SMILING = "SMILING"
    THUMBS_UP = "THUMBS UP"
    DEFAULT = "DEFAULT"


    REACTION_CHOICES = (
        (RED_HEART, _("RED HEART")),
        (FIRE, _("FIRE")),
        (SMILING, _("SMILING")),
        (THUMBS_UP, _("THUMBS UP")),
        (DEFAULT, _("DEFAULT")),
    )
