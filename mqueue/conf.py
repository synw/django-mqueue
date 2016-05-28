# -*- coding: utf-8 -*-

from django.conf import settings


EVENT_CLASSES = {
                 #~ 'Event class label' : 'css class to apply',
                'Default' : 'label label-default',
                'Important' : 'label label-warning',
                'Ok' : 'label label-success',
                'Info' : 'label label-info',
                'Debug' : 'label label-warning',
                'Warning' : 'label label-warning',
                'Error' : 'label label-danger',
                'Object created' : 'label label-primary',
                'Object edited' : 'label label-info',
                'Object deleted' : 'label label-primary',
                }

EVENT_CLASSES=getattr(settings, 'MQUEUE_EVENT_CLASSES', EVENT_CLASSES)

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
    
DEV_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'devlog':{
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'mqueue.handlers.LogsDBHandler',
            'formatter': 'verbose',
            },
        'prodlog':{
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'mqueue.handlers.LogsDBHandler',
            'formatter': 'verbose',
            },
    },
    'loggers': {
        'django': {
            'handlers': ['devlog', 'prodlog'],
            'propagate': True,
         },
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'prodlog':{
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'mqueue.handlers.LogsDBHandler',
            'formatter': 'verbose',
            },
    },
    'loggers': {
        'django': {
            'handlers': ['prodlog'],
            'propagate': True,
            
         },
    }
}
LOGGING_WARNING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'prodlog':{
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'mqueue.handlers.LogsDBHandler',
            'formatter': 'verbose',
            },
    },
    'loggers': {
        'django': {
            'handlers': ['prodlog'],
            'propagate': True,
            
         },
    }
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
