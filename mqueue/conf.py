# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _


MONITORING_LEVELS = (
                     (0, _(u"No monitoring")),
                     (1, _(u"Basic monitoring")),
                     (2, _(u"High monitoring")),
                     )

EVENT_CLASSES = {
                 #~ 'Event class label' : 'css class to apply',
                _(u'Default') : 'label label-default',
                _(u'Important') : 'label label-warning',
                _(u'Ok') : 'label label-success',
                _(u'Info') : 'label label-info',
                _(u'Debug') : 'label label-warning',
                _(u'Warning') : 'label label-danger',
                _(u'Error') : 'label label-danger',
                _(u'Object created') : 'label label-primary',
                _(u'Object edited') : 'label label-info',
                _(u'Object deleted') : 'label label-primary',
                }

EVENT_EXTRA_HTML = {
                 #~ 'Event class lable' : 'html to apply',
                }

EVENT_ICONS_HTML = {
                 #~ 'Event class label' : 'icon css class',
                _(u'Default') : '<span class="glyphicon glyphicon-flash"></span>',
                _(u'Important') : '<span class="glyphicon glyphicon-star"></span>',
                _(u'Ok') : '<span class="glyphicon glyphicon-ok"></span>',
                _(u'Info') : '<span class="glyphicon glyphicon-hand-right"></span>',
                _(u'Debug') : '<span class="glyphicon glyphicon-cog"></span>',
                _(u'Warning') : '<span class="glyphicon glyphicon-exclamation-sign"></span>',
                _(u'Error') : '<span class="glyphicon glyphicon-alert"></span>',
                _(u'Object edited') : '<span class="glyphicon glyphicon-pencil"></span>',
                _(u'Object created') : '<span class="glyphicon glyphicon-download-alt"></span>',
                _(u'Object deleted') : '<span class="glyphicon glyphicon-remove text-danger"></span>',
                }


class bcolors:
    HEADER = '\033[95m'
    PRIMARY = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'