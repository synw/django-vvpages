# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from vvpages.models import Page, UserPreference
from vvpages.forms import PageAdminWysiForm, PageAdminCodeForm
from vvpages.conf import get_editor


@admin.register(Page)
class PageAdmin(MPTTModelAdmin):
    #form = PageAdminForm
    date_hierarchy = 'edited'
    search_fields = ['title','url','editor__username']
    list_display = ['url','title','published','edited','editor']
    list_select_related = ['editor']
    list_display_links = ['title','url']
    list_filter = ['created','edited','published']
    list_select_related = ['editor']
    mptt_level_indent = 25
    save_on_top = True
    
    def get_fieldsets(self, request, obj=None):
        super(PageAdmin, self).get_fieldsets(request, obj)
        base_fields = (('url', 'title'),'parent','published')
        fieldsets = (
            (None, {
                'fields': ('content',)
            }),
            (None, {
                'fields': base_fields,
            }),
            (_(u'SEO'), {
                'classes': ('collapse',),
                'fields': ('seo_keywords','seo_description')
            }),
            (_(u'Extra data'), {
                'classes': ('collapse',),
                'fields': ('extra_data',)
            }),
        )
        return fieldsets
    
    def get_form(self, request, *args, **kwargs):
        super(PageAdmin, self).get_form(request, *args, **kwargs)
        editor = "codemirror"
        try:
            pref = UserPreference.objects.get(user=request.user)
            editor = pref.editor
        except ObjectDoesNotExist:
            editor = get_editor()
        if editor == "ckeditor":
            return PageAdminWysiForm
        else:
            return PageAdminCodeForm
        return PageAdminForm
    
    def response_change(self, request, obj):
        # for inline editing
        if '_inline_' in request.POST:
            url = obj.url.replace("%2F", "/")
            return redirect('vvpages-page', url=url)
        else:
            return super(PageAdmin, self).response_change(request, obj)
        

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
