from django.utils.translation import gettext_lazy as _


class OrderCartStatusChoices:
    """ Choices status order cart """

    NEW = "NEW"
    AWAITING = "AWAITING"
    CREATING = "CREATING"
    SHIPPING = "SHIPPING"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"

    CHOICES = (
        (NEW, _("New")),
        (AWAITING, "ожидает оплаты"),
        (CREATING, "изготовление"),
        (SHIPPING, "доставка"),
        (COMPLETED, "завершен"),
        (CANCELED, _("Canceled")),
    )
