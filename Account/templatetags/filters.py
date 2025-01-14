from django import template


register = template.Library()

@register.filter(name='count')
def count(items):
    if items is None:
        return 0
    try:
        return len(items)
    except Exception:
        return 0