Registered models
=================

.. highlight:: python

Models can be registered. They will be automaticaly monitored.

Register a model
^^^^^^^^^^^^^^^^

In ``models.py``:

::

   # myapp/models.py
   from mqueue.tracking import mqueue_tracker
   
   class TheModel(models.Model): 
      # ...
    
   mqueue_tracker.register(TheModel)


By default this will set the model to monitoring level 1 (records create
and delete). Set it to 2 if you want to record also every save on the
model:

::

   mqueue_tracker.register(TheModel, 2)


Register a foreign model
^^^^^^^^^^^^^^^^^^^^^^^^

To register a model when you don't have control over models.py do it in the ready method of the config 
class in the ``apps.py`` of your app:

::
   
   # myapp/apps.py
   from django.apps import AppConfig

   class MyappConfig(AppConfig):
       name = "myapp"
       verbose_name = "My app"
    
       def ready(self):
           from contact_form.models import Message
           from mqueue.tracking import MTracker
           #~ this will track create/delete and save actions on the Message model 
           #~ set it to 1 to track only create/delete actions
           MTracker().register(Message, 2)


