Usage
=====

Run the Centrifugo server:

.. highlight:: bash

::

   ./centrifugo --config=config.json
   
Use the ``-d`` flag for debug.

**Note**: for now events can only be broadcasted to the site public channel. This means the messages sent
this way will be visible by everyone. A private channels implementation is on the todo list.

There is two ways to broadcast events:

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

Direct broadcast of events
~~~~~~~~~~~~~~~~~~~~~~~~~~

Got to /mq/ as superuser and use the form to broadcast a message to the public channel.

By default the sent messages popup on the top-right corner of the page. The next section will describe how to 
customize the handlers on the client side according to the event class.
