from django import template

ROTATIONS = ['2.14', '-2.14', '2.14', '-2.14']

register = template.Library()


@register.filter
def get_degree(counter):
    return ROTATIONS[counter % 4]
