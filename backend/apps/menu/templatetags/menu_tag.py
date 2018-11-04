from django import template
from apps.menu.models import MenuItems

register = template.Library()


@register.simple_tag(takes_context=True)
def menu_bar(context, type_menu):
    return dict(
        nodes=MenuItems.objects.filter(menu__slug=type_menu, active=True).select_related('menu').order_by('ordering'),
        request=context['request'])
