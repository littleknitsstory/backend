from django import template
from apps.shop.models.category import Category

register = template.Library()


@register.simple_tag(name='categories_products')
def categories_products():
    return Category.objects.all().order_by('-created_at')[:5]
