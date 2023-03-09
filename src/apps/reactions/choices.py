from django.utils.translation import gettext_lazy as _


class ReactionAssociationChoices:
    ARTICLE = "ARTICLE"
    COMMENT = "COMMENT"
    COURSE = "COURSE"
    PRODUCT = "PRODUCT"

    MODEL_CHOICES = (
        (ARTICLE, _("Article")),
        (COMMENT, _("Comment")),
        (COURSE, _("Course")),
        (PRODUCT, _("Product")),
    )
