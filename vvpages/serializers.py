# -*- coding: utf-8 -*-

from rest_framework import serializers
from vvpages.models import Page


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = read_only_fields = ["content", "title", "extra_data"]
        
        
class PageEditorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = read_only_fields = ["pk", "content", "title", "extra_data"]