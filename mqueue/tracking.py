# -*- coding: utf-8 -*-

from django.db.models.signals import post_save, post_delete
from .signals import mmessage_update, mmessage_delete, mmessage_create


class MTracker(object):
    def register(self, model, monitoring_level):
        if "c" in monitoring_level:
            post_save.connect(mmessage_create, sender=model)
        if "u" in monitoring_level:
            post_save.connect(mmessage_update, sender=model)
        if "d" in monitoring_level:
            post_delete.connect(mmessage_delete, sender=model)
        return


mqueue_tracker = MTracker()
