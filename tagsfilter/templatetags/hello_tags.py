from django import template


register = template.Library()

@register.filter(name='lower')
def lower(value):
    return value.lower()


@register.filter(name='count')
def count(value):
    return len(value)


