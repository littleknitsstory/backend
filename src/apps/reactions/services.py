from src.apps.account.models import User
from django.contrib.contenttypes.models import ContentType

from .models import Reaction


def add_reactions(obj, user):
    """Ставит реакцию на `obj`."""
    obj_type = ContentType.objects.get_for_model(obj)
    reactions, is_created = Reaction.objects.get_or_create(
        model_type=obj_type, model_id=obj.id, user=user
    )
    return reactions


def remove_reactions(obj, user):
    """Удаляет реакцию с `obj`."""
    obj_type = ContentType.objects.get_for_model(obj)
    Reaction.objects.filter(model_type=obj_type, model_id=obj.id, user=user).delete()


# def is_fan(obj, user) -> bool:
#     """Проверяет, лайкнул ли user `obj`."""
#     if not user.is_authenticated:
#         return False
#     obj_type = ContentType.objects.get_for_model(obj)
#     reactions = Reaction.objects.filter(
#         model_type=obj_type, model_id=obj.id, user=user)
#     return reactions.exists()

# def get_fans(obj):
#     """Получает всех пользователей, которые лайкнули `obj`."""
#     obj_type = ContentType.objects.get_for_model(obj)
#     return User.objects.filter(
#         reactions__modelt_type=obj_type, reactions__model_id=obj.id)
