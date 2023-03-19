from django.contrib.contenttypes.models import ContentType

from .models import Reaction
from src.apps.account.models import User


def add_reactions(obj, user):
    """Add reaction to `obj`."""
    obj_type = ContentType.objects.get_for_model(obj)
    reaction, is_created = Reaction.objects.get_or_create(
        model_type=obj_type, model_id=obj.id, user=user
    )
    return reaction
