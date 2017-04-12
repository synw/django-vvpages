# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, post_delete
from jsonfield import JSONField
from mptt.models import TreeForeignKey, MPTTModel
from vvpages.conf import USER_MODEL, EDITORS
from vvpages.signals import build_assets, build_assets_del


class Seo(models.Model):
    seo_description = models.CharField(max_length=256, null=True, blank=True, verbose_name=_(u'SEO: description'), help_text=_(u'Short description of the page content'))
    seo_keywords = models.CharField(max_length=120, null=True, blank=True, verbose_name=_(u'SEO: keywords'), help_text=_(u'List of keywords separated by commas'))

    class Meta:
        abstract = True
        verbose_name=_(u'SEO')


class Page(MPTTModel, Seo):
    url = models.CharField(_(u'Url'), max_length=180, db_index=True)
    title = models.CharField(_(u'Title'), max_length=200)
    content = models.TextField(_(u'Content'), blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name=u'children', verbose_name=_(u'Parent page'))
    edited = models.DateTimeField(editable=False, null=True, auto_now=True, verbose_name=_(u'Edited'))
    created = models.DateTimeField(editable=False, null=True, auto_now_add=True, verbose_name=_(u'Created'))
    editor = models.ForeignKey(USER_MODEL, editable = False, related_name='+', null=True, on_delete=models.SET_NULL, verbose_name=_(u'Edited by'))   
    published = models.BooleanField(default=True, verbose_name=_(u'Published'))
    extra_data = JSONField(blank=True, default={}, verbose_name=_(u'Extra data'))
    
    class Meta:
        verbose_name = _(u'Page')
        verbose_name_plural = _(u'Page')
        ordering = ['url']
        
    def get_absolute_url(self):
        return self.url
    
    def __str__(self):
        return self.title
    
    
class UserPreference(models.Model):
    user = models.ForeignKey(USER_MODEL, related_name='+', null=True, on_delete=models.SET_NULL, verbose_name=_(u'User'))
    editor = models.CharField(_(u'Editor'), max_length=60, default=EDITORS[0][0], choices=EDITORS)

    
post_save.connect(build_assets, sender=Page)
post_delete.connect(build_assets_del, sender=Page)
