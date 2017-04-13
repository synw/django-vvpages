# -*- coding: utf-8 -*-

from django.core.management import call_command


def post_process(sender, instance, created, **kwargs):
    if instance.level == 1:
        call_command('build_navlinks')
    if created is True:
        instance.pageId = instance.pk
        instance.save()
    return

def post_process_del(sender, instance, **kwargs):
    if instance.level == 1:
        call_command('build_navlinks')
    return
