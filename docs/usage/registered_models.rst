Registered models
=================

.. highlight:: python

Another way to use mqueue is to register some models. They will be
automaticaly monitored.

::

   from mqueue.tracking import MTracker
   from theapp.models import TheModel

   MTracker().register(TheModel)


By default this will set the model to montoring level 1 (records create
and delete). Set it to 2 if you want to record also every save on the
model:

::

   MTracker().register(TheModel, 2)
