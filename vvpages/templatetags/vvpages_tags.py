# -*- coding: utf-8 -*-

from django import template
from vvpages.conf import CODE_MODE, LOCAL_STORAGE


register = template.Library()

@register.simple_tag
def get_edit_mode():
    if CODE_MODE == True:
        return "code"
    else:
        return "default"
    
@register.simple_tag
def use_local_storage():
    return LOCAL_STORAGE
