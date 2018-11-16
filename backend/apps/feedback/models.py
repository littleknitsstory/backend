from django.db import models
from django.utils.translation import ugettext_lazy as _

from backend.telegram_bot.bot import send_message


class Feedback(models.Model):
    """ Feedback model """
    name = models.CharField(_('Name'), max_length=120)
    email = models.EmailField(_('Email'))
    feedback = models.TextField(_('Feedback'))

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Feedback, self).save(
            force_insert, force_update, using, update_fields
        )
        send_message(
            "Новое обращение к администрации сайта:\n" + self.feedback
        )

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __str__(self):
        return self.feedback[:25]
