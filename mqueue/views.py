# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.views.generic import FormView
from django.views.generic.base import RedirectView
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from mqueue.models import MEvent
from mqueue.forms import BroadcastForm


class BroadcastView(FormView):
    form_class = BroadcastForm
    template_name = 'mqueue/broadcast.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404
        return super(BroadcastView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        msg = form.cleaned_data['message']
        event_class = form.cleaned_data['event_class']
        channel = form.cleaned_data['channel']
        MEvent.objects.create(name=msg, event_class=event_class, commit=False, stream=True, channel=channel)
        messages.info(self.request, _(u"Message broadcasted to channel "+channel))
        return super(BroadcastView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('mqueue-message-broadcasted')


