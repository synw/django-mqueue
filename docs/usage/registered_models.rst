Registered models
=================

.. highlight:: python

Models can be registered. They will be automaticaly monitored.

Register a model
^^^^^^^^^^^^^^^^

::

   from mqueue.tracking import mqueue_tracker
   from myapp.models import TheModel
    
   mqueue_tracker.register(TheModel)


By default this will set the model to monitoring level 1 (records create
and delete). Set it to 2 if you want to record also every save on the
model:

::

   mqueue_tracker.register(TheModel, 2)



