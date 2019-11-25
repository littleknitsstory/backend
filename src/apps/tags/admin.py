from django.contrib import admin
from src.apps.tags.models import Tag
from src.core.mixins.mixin import AdminBaseMixin


@admin.register(Tag)  # noqa
class AdminTag(AdminBaseMixin):  # noqa
    """
    Tags admin
    """
    pass
