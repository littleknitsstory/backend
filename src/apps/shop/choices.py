from django.utils.translation import gettext_lazy as _


class OrderCartStatusChoices:
    """Choices status order cart"""

    NEW = "NEW"
    AWAITING = "AWAITING"
    CREATING = "CREATING"
    SHIPPING = "SHIPPING"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"

    CHOICES = (
        (NEW, _("New")),
        (AWAITING, _("Awaiting pay")),
        (CREATING, _("Creating")),
        (SHIPPING, _("Shipping")),
        (COMPLETED, _("Completed")),
        (CANCELED, _("Canceled")),
    )


class ProductTypeChoices:
    """Choices Product type"""

    HANDMADE = "HANDMADE"
    SUBSCRIBE = "SUBSCRIBE"
    COURSE = "COURSE"
    SCHEMA = "SCHEMA"

    CHOICES = (
        (HANDMADE, _("Handmade")),
        (SUBSCRIBE, _("Subscribe")),
        (COURSE, _("Course")),
        (SCHEMA, _("Schema")),
    )
