Watchers
========

Some watchers connected to signals are available. Declare the ones you want to use in settings:

.. highlight:: python

::

   MQUEUE_WATCH = ["login", "logout", "login_failed"]
   
   # Warning: the line above must be before registering the loggers
   from mqueue.conf import LOGGING


The events will be fired accordingly, same way than registering models