from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by the given argument and strip whitespace from each item"""
    if not value:
        return []
    return [item.strip() for item in value.split(arg) if item.strip()]
