# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

USE_REVERSION=getattr(settings, 'VVPAGES_USE_REVERSION', "reversion" in settings.INSTALLED_APPS)

BASE_TEMPLATE_PATH = getattr(settings, 'VVPAGES_BASE_TEMPLATE_PATH', 'base.html')

CODE_MODE = getattr(settings, 'VVPAGES_CODE_MODE', False)
CODEMIRROR_KEYMAP = getattr(settings, 'VVPAGES_CODEMIRROR_KEYMAP', 'default')

EDITORS = (
    ("codemirror", "Codemirror"),
    ("ckeditor", "Ckeditor")
    )

def get_editor():
    if CODE_MODE is True:
        return "codemirror"
    else:
        return "ckeditor"

LOCAL_STORAGE = getattr(settings, 'VVPAGES_LOCAL_STORAGE', False)
