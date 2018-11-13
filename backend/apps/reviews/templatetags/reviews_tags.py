from django import template
from ..models import Review

register = template.Library()


@register.simple_tag(name='reviews')
def review_tag():
    return Review.objects.all()
