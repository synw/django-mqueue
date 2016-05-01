# -*- coding: utf-8 -*-

from django.db.models.signals import post_save, post_delete
from mqueue.signals import mmessage_save, mmessage_delete, mmessage_create
  

class MTracker(object):

    def register(self, model , monitoring_level=1):
        if monitoring_level == 1:
            post_save.connect(mmessage_create, sender=model)
        if monitoring_level == 2:
            post_save.connect(mmessage_save, sender=model)
        post_delete.connect(mmessage_delete, sender=model)
        return
    
mqueue_tracker = MTracker()