# -*- coding: utf-8 -*-

from django.conf.urls import url
from mqueue.views import EventsDash


urlpatterns = [
    url(r'^', EventsDash.as_view(), name="mqueue-dashboard")
]
