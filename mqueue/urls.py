# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from mqueue.views import BroadcastView


urlpatterns = patterns('',
    url(r'^redirect-home/$', RedirectView.as_view(url=reverse_lazy('mqueue-broadcast')), name='mqueue-message-broadcasted'),
    #url(r'^ok/$', MessageBroadcastedView.as_view(pattern_name='mqueue-message-broadcasted'), name="mqueue-message-broadcasted"),
    url(r'^', BroadcastView.as_view(), name="mqueue-broadcast"),
)
