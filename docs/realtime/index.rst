Usage
=====

Install `Django Mqueue Livefeed <https://github.com/synw/django-mqueue-livefeed/>`_

Autostream events and logs
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once Django Mqueue Livefeed installed all the registered models events and the logs will be broadcasted to a private
channel and can be seen via a dashboard at `/events/`.


Stream events into a private channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. highlight:: python

::

   from mqueue.models import MEvent

   # fire an event on the public channel
   MEvent.objects.create(name='Hello world', stream=True, channel="$private", commit=False, event_class="Infos")
   
The ``stream=True`` parameter is required to stream the event, ``commit=False`` is 
to tell mqueue not to save the event into the database. Do not set if you want 
it recorded in the db as well.

Note: if stream is True and no channel is provided the event will be pushed to the default public channel set
in django-instant.

