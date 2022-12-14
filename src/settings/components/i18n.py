import os

from django.utils.translation import gettext_lazy as _

from src.settings.components._paths import BASE_DIR

LANGUAGE_CODE = "ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_L10N = True
USE_TZ = True
FORMAT_TZ = "%m/%d/%Y, %H:%M:%S"
ADMIN_LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
)
MODELTRANSLATION_LANGUAGES = (
    "ru",
    "en",
)
MODELTRANSLATION_DEFAULT_LANGUAGE = "en"
LOCALE_PATHS = (
    os.path.join(os.path.dirname(BASE_DIR), "locale"),  # src/locale
    os.path.join(os.path.dirname(BASE_DIR), "locale_tpa"),
)
