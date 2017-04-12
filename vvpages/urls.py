# -*- coding: utf-8 -*-

from django.conf.urls import url
from vvpages.views import SitemapRestView


urlpatterns = [
    url(r'^sitemaprest/$', SitemapRestView.as_view(), name="vvpages-map-rest"),
    ]