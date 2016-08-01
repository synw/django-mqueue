Usage
=====

Install `django-instant <https://github.com/synw/django-instant/>`_ and run it

Stream events from code
~~~~~~~~~~~~~~~~~~~~~~~ 

.. highlight:: python

::

   from mqueue.models import MEvent

   # fire an event on the public channel
   MEvent.objects.create(name='Hello world', stream=True, commit=False, event_class="Infos")
   
The ``stream=True`` parameter is required to stream the event, ``commit=False`` is 
to tell mqueue not to save the event into the database. Do not set if you want 
it recorded in the db as well.

