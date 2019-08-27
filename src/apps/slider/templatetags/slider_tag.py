from django import template

from apps.slider.models import Slider

register = template.Library()


@register.simple_tag
def get_slider():
    slider = Slider.objects.filter(active=True)
    return slider
