# -*- coding: utf-8 -*-

from django.core.management import call_command


def build_assets(sender, instance, created, **kwargs):
    if instance.level == 1:
        call_command('build_navlinks')
    call_command('build_routes')
    return

def build_assets_del(sender, instance, **kwargs):
    if instance.level == 1:
        call_command('build_navlinks')
    call_command('build_routes')
    return
