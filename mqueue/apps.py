from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig
import inspect


def tracking_load_registry(*args, **kwargs):
    """
    Thanks to https://github.com/emencia/emencia-django-tracking
    """
    stack = inspect.stack()

    for stack_info in stack[1:]:
        if 'tracking_load_registry' in stack_info[3]:
            return
        

class MqueueConfig(AppConfig):
    name = "mqueue"
    verbose_name = _(u"Events queue")
    
    def ready(self):
        from mqueue import signals
        tracking_load_registry()
        
        