# -*- coding: utf-8 -*-

from django import template
from vvpages.conf import LOCAL_STORAGE


register = template.Library()
    
@register.simple_tag
def use_local_storage():
    return LOCAL_STORAGE
