from django import template
from apps.shop.models.product import Product

register = template.Library()


@register.simple_tag(name='most_popular_products')
def most_popular_products():
    return Product.objects.all().order_by('?')[:4]
