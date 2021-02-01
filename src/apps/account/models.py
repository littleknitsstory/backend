import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from optimized_image.fields import OptimizedImageField

from src.apps.account.choices import AccountTypeChoices
from src.core.utils.send_mail import send_email_celery


class User(AbstractUser):
    """ """

    account_type = models.CharField(
        _("Type user"),
        choices=AccountTypeChoices.USER_CHOICES,
        default=AccountTypeChoices.CLIENT,
        max_length=63,
    )
    avatar = OptimizedImageField(_("Avatar"), null=True, blank=True)
    about = models.TextField(_("About author"), max_length=633, null=True, blank=True)

    phone_number = models.CharField(
        _("Phone number"), max_length=13, null=True, blank=True
    )
    country = CountryField(
        verbose_name=_("Country"), default=None, null=True, blank=True
    )
    city = models.CharField(_("City"), max_length=63, null=True, blank=True)
    address = models.CharField(_("Address"), max_length=512, null=True, blank=True)
    birth_date = models.DateField(_("Birth date"), null=True, blank=True)

    is_email_confirmed = models.BooleanField(_("Email confirm"), default=False)
    is_profile_full = models.BooleanField(_("Profile full"), default=False)
    vk_profile = JSONField(_("Vk profile"), blank=True, null=True)
    fb_profile = JSONField(_("Fb profile"), blank=True, null=True)
    inst_profile = JSONField(_("Instagram profile"), blank=True, null=True)
    tg_profile = JSONField(_("Telegram profile"), blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def get_avatar_url(self):
        try:
            return self.avatar.url
        except ValueError:
            return None

    @property
    def fb_link(self):
        if self.fb_profile:
            return self.fb_profile.get("link")

    @property
    def vk_link(self):
        if self.vk_profile:
            return self.vk_profile.get("link")

    @property
    def inst_link(self):
        if self.inst_profile:
            return self.inst_profile.get("link")

    def get_country(self):
        return {"name": self.country.name, "code": self.country.code}

    def send_confirm(self):
        # TODO: need templates for welcome mail
        code = set_code(self.email.lower())
        message = f"{code}"
        send_email_celery.delay(to=[self.email], subject=_("Welcome"), message=message)


# TODO: go utils
def set_code(email):
    key = str(uuid.uuid4()).replace("-", "")
    # settings.REDIS_CONNECT.set(email, key, ex=300)
    return key


def get_code(key):
    return settings.REDIS_CONNECT.get(key)
