from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.postgres.fields import JSONField
from django_countries.fields import CountryField

from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from optimized_image.fields import OptimizedImageField

from src.apps.users.choices import AccountTypeChoices


class User(AbstractUser):

    account_type = models.CharField(_('Type user'), choices=AccountTypeChoices.USER_CHOICES, max_length=63)
    avatar = OptimizedImageField(_('Avatar'), null=True, blank=True)
    about = models.TextField(_('About author'), max_length=633, null=True, blank=True)
    
    phone_number = models.CharField(_('Phone number'), max_length=63, null=True, blank=True)
    country = CountryField(verbose_name=_('Country'), default=None, null=True, blank=True)

    city = models.CharField(_('City'), max_length=63, null=True, blank=True)
    birth_date = models.DateField(_('Birth date'), null=True, blank=True)
    
    is_email_confirmed = models.BooleanField(_('Email confirm'), default=False)
    is_profile_full = models.BooleanField(_('Profile full'), default=True)
    vk_profile = JSONField(_('Vk profile'), blank=True, null=True)
    fb_profile = JSONField(_('Fb profile'), blank=True, null=True)
    inst_profile = JSONField(_('Instagram profile'), blank=True, null=True)
    tg_profile = JSONField(_('Telegram profile'), blank=True, null=True)

    objects = UserManager()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        app_label = 'user_2'

    def get_avatar_url(self):
        try:
            return self.avatar.url
        except ValueError:
            return None

    @property
    def fb_link(self):
        if self.fb_profile:
            return self.fb_profile.get('link')

    @property
    def vk_link(self):
        if self.vk_profile:
            return f'https://vk.com/id{self.vk_profile.get("id")}'
