# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from mqueue.views import MQueueView


urlpatterns = patterns('',
    url(r'^', MQueueView.as_view(), name="mqueue-view"),
)
