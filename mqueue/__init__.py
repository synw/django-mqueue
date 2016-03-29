__version__ = '0.3'
default_app_config = 'mqueue.apps.MqueueConfig'

import inspect

"""
Thanks to https://github.com/emencia/emencia-django-tracking
"""

from mqueue.tracking import MTracker

tracking = MTracker()

def tracking_load_registry(*args, **kwargs):
    stack = inspect.stack()

    for stack_info in stack[1:]:
        if 'tracking_load_registry' in stack_info[3]:
            return

tracking_load_registry()

