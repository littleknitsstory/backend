from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.postgres.fields import JSONField
from django_countries.fields import CountryField

from django.db import models
from django.utils.translation import gettext_lazy as _
from optimized_image.fields import OptimizedImageField

from src.apps.account.choices import AccountTypeChoices


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)

    account_type = models.CharField(
        _("Type user"), choices=AccountTypeChoices.USER_CHOICES, max_length=63
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

    # TODO: надо перехать на было только
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

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

    def get_country(self, user=None):
        return {"name": self.country.name, "code": self.country.code}
