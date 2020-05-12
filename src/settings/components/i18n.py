import os

from django.utils.translation import ugettext_lazy as _

from src.settings.components._paths import BASE_DIR

LANGUAGE_CODE = "ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True
USE_TZ = True
FORMAT_TZ = "%m/%d/%Y, %H:%M:%S"

ADMIN_LANGUAGE_CODE = "ru"

LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
)

MODELTRANSLATION_LANGUAGES = (
    "ru",
    "en",
)
MODELTRANSLATION_DEFAULT_LANGUAGE = "ru"

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
    os.path.join(BASE_DIR, "locale_tpa"),
)
