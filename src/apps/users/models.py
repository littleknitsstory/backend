import uuid

from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.postgres.fields import JSONField

from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from optimized_image.fields import OptimizedImageField
from phonenumber_field.modelfields import PhoneNumberField

from core.utils.choices import AccountTypeChoices


class User(AbstractUser):

    jwt_secret = models.UUIDField(_('jwt_secret'), default=uuid.uuid4)
    account_type = models.CharField(_('Type user'), choices=AccountTypeChoices.USER_CHOICES, max_length=63)
    username = models.CharField(_('Username'), unique=True, null=True, blank=True, max_length=63)
    avatar = OptimizedImageField(_('Avatar'), null=True, blank=True)
    phone_number = PhoneNumberField(_('Phone number'), null=True, blank=True)
    country = models.CharField(_('Country'), max_length=63, null=True, blank=True)
    city = models.CharField(_('City'), max_length=63, null=True, blank=True)
    birth_date = models.DateField(_('Birth date'), null=True, blank=True)
    email = models.EmailField(_('Email'), unique=True)
    is_email_confirmed = models.BooleanField(_('Email confirm'), default=False)
    is_profile_full = models.BooleanField(_('Profile full'), default=True)
    vk_profile = JSONField(_('Vk profile'), blank=True, null=True)
    fb_profile = JSONField(_('Fb profile'), blank=True, null=True)
    
    objects = UserManager()

    def get_jwt_secret(self):
        return self.jwt_secret

    def get_photo_url(self):
        """
        :return:
        """
        try:
            return self.photo.url
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
        
    def get_absolute_url(self):
        return reverse_lazy('profile:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
