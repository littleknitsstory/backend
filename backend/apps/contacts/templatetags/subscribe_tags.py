from django import template
from apps.contacts.forms.subscribe import SubscribeForm

register = template.Library()


@register.simple_tag(name='subscribe')
def review_tag():
    return SubscribeForm()