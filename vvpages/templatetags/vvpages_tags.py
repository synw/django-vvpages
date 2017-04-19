# -*- coding: utf-8 -*-

from django import template
from vvpages.conf import LOCAL_STORAGE, SITE_SLUG, TTL


register = template.Library()
    
@register.simple_tag
def use_local_storage():
    return LOCAL_STORAGE

@register.simple_tag
def site_slug():
    return SITE_SLUG

@register.simple_tag
def ttl():
    return TTL
