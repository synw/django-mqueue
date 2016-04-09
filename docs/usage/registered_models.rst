Registered models
=================

.. highlight:: python

Another way to use mqueue is to register some models. They will be
automaticaly monitored.

Register a model
^^^^^^^^^^^^^^^^

In ``models.py``:

::

   # myapp/models.py
   from mqueue.tracking import MTracker
   
   class TheModel(models.Model): 
      # ...
    
   MTracker().register(TheModel)


By default this will set the model to monitoring level 1 (records create
and delete). Set it to 2 if you want to record also every save on the
model:

::

   MTracker().register(TheModel, 2)


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
           MTracker().register(Message, 2)


