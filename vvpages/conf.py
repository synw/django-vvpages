# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

USE_REVERSION=getattr(settings, 'VUEPAGES_USE_REVERSION', "reversion" in settings.INSTALLED_APPS)

BASE_TEMPLATE_PATH = getattr(settings, 'VUEPAGES_BASE_TEMPLATE_PATH', 'base.html')

CODE_MODE = getattr(settings, 'VUEPAGES_CODE_MODE', False)
CODEMIRROR_KEYMAP = getattr(settings, 'VUEPAGES_CODEMIRROR_KEYMAP', 'default')