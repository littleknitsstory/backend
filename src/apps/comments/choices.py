
class CommentAssociationChoices:
    ARTICLE = "ARTICLE"
    COMMENT = "COMMENT"
    COURSE = "COURSE"
    PRODUCT = "PRODUCT"

    MODEL_CHOICES = (
        (ARTICLE, "Article"),
        (COMMENT, "Comment"),
        (COURSE, "Course"),
        (PRODUCT, "Product"),
    )
