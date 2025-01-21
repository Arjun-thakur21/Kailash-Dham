from django import template

register = template.Library()

@register.filter(name='word_limit')
def word_limit(value, limit=50):
    words = value.split()[:limit]
    return ' '.join(words) + '...'
