# -*- coding: utf-8 -*-

from django.conf.urls import url
from vvpages.views import PageRestView, SitemapRestView, PageWizardView, AddPagePostView


urlpatterns = [
    #url(r'^map/$', SitemapView.as_view(), name="vvpages-map"),
    url(r'^sitemaprest/$', SitemapRestView.as_view(), name="vvpages-map-rest"),
    url(r'^rest/(?P<pk>[0-9]+)/$', PageRestView.as_view(), name="vvpages-rest"),
    url(r'^wizard/rest/$', PageWizardView.as_view(), name="vvpages-wizard"),
    url(r'^wizard/post/$', AddPagePostView.as_view(), name="vvpages-wizard-post")
    ]