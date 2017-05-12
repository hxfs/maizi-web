# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.filter(name='add_img_url')
def add_img_url(value):
    """
    完善url路径

    """
    value = 'static/images/uploads/' + str(value)
    return value


@register.filter(name='splite_list')
def splite_list(value, arg):
    index = ["A", "B", "C"]
    if arg in index:
        value = value[index.index(arg)]
        return value
    else:
        pass


@register.assignment_tag(name='splite_list_1')
def splite_list(value, arg):
    value = value[arg]
    return value
