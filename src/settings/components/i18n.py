from django.utils.translation import ugettext_lazy as _


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MODELTRANSLATION_LANGUAGES = ('ru', 'en')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

gettext = lambda s: s  # noqa

LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    ROOT_DIR + '/locale', )
