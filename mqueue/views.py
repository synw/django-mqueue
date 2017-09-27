# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class EventsDash(TemplateView):
    template_name = "mqueue/dashboard.html"