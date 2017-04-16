# -*- coding: utf-8 -*-

import json
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from vvpages.serializers import PageSerializer, PageEditorSerializer
from vvpages.models import Page


class PageRestView(APIView):
    
    def get_object(self, id):
        try:
            return get_object_or_404(Page, pk=self.kwargs['pk'], published=True)
        except Page.DoesNotExist:
            raise Http404
    
    def get(self, request, *args, **kwargs):
        page = self.get_object(id)
        if self.request.user.has_perm("vvpages_change_page"):
            serializer = PageEditorSerializer(page)
        else:
            serializer = PageSerializer(page)
        return Response(serializer.data)
    
    def get_queryset(self, *args, **kwargs):
        q = Page.objects.filter(pk=self.kwargs['pk'], published=True)
        return q


class SitemapRestView(TemplateView):
    template_name = "vvpages/sitemap.html"
    
    def get_context_data(self, **kwargs):
        context = super(SitemapRestView, self).get_context_data(**kwargs)
        root_node, created = Page.objects.get_or_create(url="/")
        if created is True:
            root_node.title = "Home"
            root_node.save()
        nodes = root_node.get_descendants(include_self=True).filter(published=True)
        context['nodes'] = nodes
        return context


class AddPagePostView(TemplateView):
    template_name = "vvpages/wizard/tree_inline.html"

    def get_context_data(self, **kwargs):
        context = super(AddPagePostView, self).get_context_data(**kwargs)
        root_node = Page.objects.get(url="/")
        nodes = root_node.get_descendants(include_self=True)
        context['nodes'] = nodes
        context["flashnode"] = self.newnode.pk
        return context
    
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode('utf-8'))
        parent = Page.objects.get(url=data["parent"])
        self.newnode = Page.objects.create(url=data["url"], title=data["title"], parent=parent, editor=request.user)
        if not request.user.has_perm('vvpages.change_page') or not self.request.method == "POST":
            raise Http404
        data = render(request, "vvpages/wizard/tree_inline.html", context=self.get_context_data())
        return data


class PageWizardView(TemplateView):
    template_name = "vvpages/wizard/index.html"
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vvpages.change_page'):
            raise Http404
        return super(PageWizardView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PageWizardView, self).get_context_data(**kwargs)
        root_node, created = Page.objects.get_or_create(url="/")
        nodes = root_node.get_descendants(include_self=True)
        context['nodes'] = nodes
        return context
