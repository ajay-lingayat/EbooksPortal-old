from django import template

register = template.Library()

@register.filter(name='lnk_filter')
def lnk_filter(value):
    return value.replace('blob', 'raw')