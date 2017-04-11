# -*- coding: utf-8 -*-

from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from vvpages.serializers import PageSerializer
from vvpages.models import Page


class PageRestView(APIView):
    
    def get_object(self, id):
        try:
            return get_object_or_404(Page, pk=self.kwargs['pk'], published=True)
        except Page.DoesNotExist:
            raise Http404
    
    def get(self, request, *args, **kwargs):
        page = self.get_object(id)
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
    
class PageWizardView(TemplateView):
    template_name = "vvpages/wizard/index.html"
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('alapage.change_page'):
            raise Http404
        return super(PageWizardView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PageWizardView, self).get_context_data(**kwargs)
        context["template_to_extend"] = BASE_TEMPLATE_PATH
        root_node, created = Page.objects.get_or_create(url="/")
        nodes = root_node.get_descendants(include_self=True)
        context['nodes'] = nodes
        return context    

