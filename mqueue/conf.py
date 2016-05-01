# -*- coding: utf-8 -*-

import collections
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


MONITORING_LEVELS = [
                     (0, _(u"No monitoring")),
                     (1, _(u"Basic monitoring")),
                     (2, _(u"High monitoring")),
                     ]

OBJECT_LEVEL_DEFAULT_MONITORING = getattr(settings, 'MQUEUE_OBJECT_LEVEL_DEFAULT_MONITORING', 1)

MODELS_NOT_TO_MONITOR = getattr(settings, 'MQUEUE_STOP_MONITORING', [])

EVENT_CLASSES = {
                 #~ 'Event class label' : 'css class to apply',
                'Default' : 'label label-default',
                'Important' : 'label label-warning',
                'Ok' : 'label label-success',
                'Info' : 'label label-info',
                'Debug' : 'label label-warning',
                'Warning' : 'label label-danger',
                'Error' : 'label label-danger',
                'Object created' : 'label label-primary',
                'Object edited' : 'label label-info',
                'Object deleted' : 'label label-primary',
                }

EVENT_CLASSES=getattr(settings, 'MQUEUE_EVENT_CLASSES', EVENT_CLASSES)

EVENT_CHOICES = []
event_classes = collections.OrderedDict(sorted(EVENT_CLASSES.items()))
for event_class in event_classes.keys():
    EVENT_CHOICES.append( ( event_class, event_class ) )

EVENT_ICONS_HTML = {
                 #~ 'Event class label' : 'icon css class',
                'Default' : '<span class="glyphicon glyphicon-flash"></span>',
                'Important' : '<span class="glyphicon glyphicon-star"></span>',
                'Ok' : '<span class="glyphicon glyphicon-ok"></span>',
                'Info' : '<span class="glyphicon glyphicon-hand-right"></span>',
                'Debug' : '<span class="glyphicon glyphicon-cog"></span>',
                'Warning' : '<span class="glyphicon glyphicon-exclamation-sign"></span>',
                'Error' : '<span class="glyphicon glyphicon-alert"></span>',
                'Object edited' : '<span class="glyphicon glyphicon-pencil"></span>',
                'Object created' : '<span class="glyphicon glyphicon-download-alt"></span>',
                'Object deleted' : '<span class="glyphicon glyphicon-remove text-danger"></span>',
                }

EVENT_ICONS_HTML=getattr(settings, 'MQUEUE_EVENT_ICONS_HTML', EVENT_ICONS_HTML)

EVENT_EXTRA_HTML=getattr(settings, 'MQUEUE_EVENT_EXTRA_HTML', {})

class bcolors:
    HEADER = '\033[95m'
    PRIMARY = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

