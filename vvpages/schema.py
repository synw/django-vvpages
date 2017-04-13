# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from vvpages.models import Page


class PageNode(DjangoObjectType):
    class Meta:
        model = Page
        only_fields = ("url", "title", "content", "extra_data")
        filter_fields = {
            'url' : ['exact'],
            'title' : ['icontains', 'istartswith'],
            }
        interfaces = (relay.Node, )


class Query(graphene.AbstractType):
    all_pages = DjangoFilterConnectionField(PageNode)
    page = graphene.Field(PageNode,
                              id=graphene.Int(),
                              url=graphene.String())
    
    def resolve_all_pages(self, args, context, info):
        return Page.objects.filter(published=True)

    def resolve_page(self, args, context, info):
        url = args.get('url')
        title = args.get("title")
        if url is not None:
            try:
                page = Page.objects.get(url=url)
            except Page.DoesNotExist:
                if url == "/":
                    home = _("Homepage")
                    page = Page.objects.create(url=url, title=home)
                else:
                    page = Page.objects.get(url="/404/")
        return page
