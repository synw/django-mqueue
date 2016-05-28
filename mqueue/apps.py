import importlib
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class MqueueConfig(AppConfig):
    name = "mqueue"
    verbose_name = _(u"Events queue")
    
    def ready(self):
        from mqueue import signals
        # models registration from settings
        from django.conf import settings
        from mqueue.tracking import mqueue_tracker
        AUTOREGISTER = getattr(settings, 'MQUEUE_AUTOREGISTER', [])
        for modtup in AUTOREGISTER:
            modpath = modtup[0]
            level = modtup[1]
            modsplit = modpath.split('.')
            path = '.'.join(modsplit[:-1])
            modname = '.'.join(modsplit[-1:])
            module = importlib.import_module(path)
            model = getattr(module, modname)
            mqueue_tracker.register(model, level)
            
        
        
        