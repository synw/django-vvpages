# -*- coding: utf-8 -*-

from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
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
