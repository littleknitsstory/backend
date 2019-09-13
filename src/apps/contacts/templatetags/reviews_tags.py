from django import template
from apps.contacts.models import Review

register = template.Library()


@register.simple_tag(name='reviews')
def review_tag():
    return Review.objects.all()
