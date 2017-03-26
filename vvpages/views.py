# -*- coding: utf-8 -*-

import json
from django.views.generic.base import View
from django.http import JsonResponse
from django.conf import settings
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from instant.producers import publish


class PostMsgView(LoginRequiredMixin, SuperuserRequiredMixin, View):
    login_url = settings.LOGIN_URL
    
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode('utf-8'))
        msg = data["msg"]
        channel = data["channel"]
        event_class = data["event_class"]
        publish(message=msg, event_class=event_class, channel=channel)
        return JsonResponse({"ok":1})
