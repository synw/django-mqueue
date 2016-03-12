# -*- coding: utf-8 -*-


EVENT_CLASSES = {
                 #~ 'Event class label' : 'css class to apply',
                'Default' : 'label label-default',
                'Important' : 'label label-primary',
                'Ok' : 'label label-success',
                'Info' : 'label label-info',
                'Debug' : 'label label-warning',
                'Warning' : 'label label-danger',
                'Error' : 'label label-danger',
                'Object created' : 'label label-primary',
                'Object edited' : 'label label-info',
                'Object deleted' : 'label label-warning',
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