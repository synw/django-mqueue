Logs handler
============

Mqueue has a log handler that to stores the django logs into the db as events.

To enable it add this to `settings.py`

.. highlight:: python

::

   from mqueue.conf import LOGGING
   
This will enable logging on ERROR level when `DEBUG` is False. To log on WARNING level do this:

::

   from mqueue.conf import LOGGING_WARNING as LOGGING
   
To enable logging when `DEBUG` is True or False:

::

   from mqueue.conf import DEV_LOGGING as LOGGING
   
   