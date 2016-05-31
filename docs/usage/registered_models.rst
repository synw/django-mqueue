Registered models
=================

.. highlight:: python

Models can be registered. They will be automaticaly monitored.

Autoregister a model
^^^^^^^^^^^^^^^^^^^^

In ``settings.py``:

::

   MQUEUE_AUTOREGISTER = (
   						#('app.module.model', registration level: 1=create+delete, 2=1+save),
                       	('django.contrib.auth.models.User', 1),
                       	('alapage.models.Page', 2),
                       	)

The registered modules will be monitored.

Manualy register a model
^^^^^^^^^^^^^^^^^^^^^^^^

In any installed app ``apps.py`` :

::

   from django.apps import AppConfig
   
   class DjConfig(AppConfig):
       name = "myapp"
       verbose_name = "My app"
       
       def ready(self):
           from mqueue.tracking import mqueue_tracker
           from myapp.models import TheModel
    
           mqueue_tracker.register(TheModel)


By default this will set the model to monitoring level 1 (records create
and delete). Set it to 2 if you want to record also every save on the
model:

::

   mqueue_tracker.register(TheModel, 2)



