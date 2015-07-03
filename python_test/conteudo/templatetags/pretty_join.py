# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.template.base import Library
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = Library()


def _as_link(obj):
    if hasattr(obj, 'get_absolute_url'):
        return '<a href="{0}">{1}</a>'.format(obj.get_absolute_url(),
                                              force_text(obj))
    else:
        return force_text(obj)


@register.filter
def pretty_join(value, conjuncao='e'):
    value = list(value)  # force evaluation

    if len(value) == 0:
        return ''

    if len(value) == 1:
        return mark_safe(_as_link(value[0]))

    lista, ultimo = value[:-1], value[-1]
    lista = ', '.join(_as_link(l) for l in lista)

    return mark_safe('{0} {1} {2}'.format(lista, conjuncao, _as_link(ultimo)))
