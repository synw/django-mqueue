Logs handler
============

Mqueue has a log handler that to stores the django logs into the db as events.

To enable it add this to ``settings.py``

.. highlight:: python

::

   from mqueue.logging import LOGGING
   
This will enable logging on ERROR level when ``DEBUG`` is ``False``. To log on WARNING level 
(which also handles the the 404 errors and friends) do this:

::

   from mqueue.logging import LOGGING_WARNING as LOGGING
   
To enable logging in dev mode, when ``DEBUG`` is ``True`` or ``False`` (useful to debug some ajax for example):

::

   from mqueue.logging import DEV_LOGGING as LOGGING
   
   