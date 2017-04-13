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
            }
        interfaces = (relay.Node, )


class Query(graphene.AbstractType):
    page = graphene.Field(PageNode,
                              id=graphene.Int(),
                              url=graphene.String())

    def resolve_page(self, args, context, info):
        url = args.get('url')
        if url is not None:
            try:
                if url == "/":
                    home = _("Homepage")
                    page, created = Page.objects.get_or_create(url=url, title=home)
                else:
                    page = Page.objects.get(url=url)
            except Page.DoesNotExist:
                page = Page.objects.get(url="/404/")
        return page
        return None
