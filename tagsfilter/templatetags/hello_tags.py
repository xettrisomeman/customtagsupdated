from django import template
from ..models import Name

register = template.Library()

@register.filter(name='lower')
def lower(value):
    return value.lower()


@register.filter(name='count')
def count(value):
    return len(value)


#inclusion tag returns dictionary
@register.inclusion_tag("tagsfilter/details.htm")
def show_details(count):
    posts = Name.objects.all()[:count] 
    return {
        "posts": posts,
    }
