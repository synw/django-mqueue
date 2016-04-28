from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class MqueueConfig(AppConfig):
    name = "mqueue"
    verbose_name = _(u"Events queue")
    
    def ready(self):
        from mqueue import signals
        
        