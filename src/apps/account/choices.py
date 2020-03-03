from django.utils.translation import ugettext_lazy as _


class AccountTypeChoices:
    AUTHOR = "AUTHOR"
    MANAGER = "MANAGER"
    CLIENT = "CLIENT"

    USER_CHOICES = (
        (AUTHOR, _("Author")),
        (MANAGER, _("Manager")),
        (CLIENT, _("Client")),
    )
