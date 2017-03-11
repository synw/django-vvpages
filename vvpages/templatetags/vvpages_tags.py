# -*- coding: utf-8 -*-

from django import template
from spages.conf import CODE_MODE


register = template.Library()

@register.simple_tag
def get_edit_mode():
    if CODE_MODE == True:
        return "code"
    else:
        return "default"