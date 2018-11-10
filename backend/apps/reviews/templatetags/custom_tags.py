from django import template

register = template.Library()

from ..models import Product, Review

@register.simple_tag(name = 'review_count')
def review_counter():
    return Review.objects.count()