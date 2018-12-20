from django import template
from apps.blog.models import Article

register = template.Library()


@register.simple_tag(name='last_posts')
def last_posts():
    return Article.objects.all()[:3]
