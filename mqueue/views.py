# -*- coding: utf-8 -*-
"""
from django.views.generic import ListView
from mqueue.models import MEvent


class MQueueView(ListView):
    template_name = 'mqueue/view_queue.html'
    paginate_by = 50
    context_object_name = 'events'
    
    def get_queryset(self):
        qs = MEvent.objects.all()
        print "user="+str(self.request.user)
        return qs
"""