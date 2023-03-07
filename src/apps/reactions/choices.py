from django.utils.translation import gettext_lazy as _


class ReactionAssociationChoices:
    ARTICLE = "ARTICLE"
    COMMENT = "COMMENT"
    COURSE = "COURSE"
    PRODUCT = "PRODUCT"
    # добавила
    REACTION = "REACTION"

    MODEL_CHOICES = (
        (ARTICLE, _("Article")),
        (COMMENT, _("Comment")),
        (COURSE, _("Course")),
        (PRODUCT, _("Product")),
        # добавила
        (REACTION, _("Reaction")),
    )
