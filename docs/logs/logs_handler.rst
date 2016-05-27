Logs handler
============

Mqueue has a log handler that you can use to store the django logs in the db.

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
   
   