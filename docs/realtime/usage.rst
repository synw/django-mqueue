Usage
=====

To run the nodejs/socketio server: copy the mqueue/wsocks folder where you want it, cd to the folder and run the server:

Get the js requirements with ``npm install express socket.io redis``
Configure on top of the file wsocks.js at least the SITE_SLUG with the same you put in settings.py

Then run ``nodejs wsocks.js``

Stream events from code
~~~~~~~~~~~~~~~~~~~~~~~

Then you can send events in channels from your code. There are 4 channels available: *public* (everyone), *user* (everyone 
minus anonymous users), *staff* (admins and staff) and *admin* (only admins). 

.. highlight:: python

::

   from mqueue.models import MEvent 

   # fire an event on the public channel
   MEvent.objects.create(name='Hello world', stream=True, commit=False, channel='public', event_class="Infos")
   
The ``commit=False`` is to tell mqueue not to save the event into the database. Do not set if you want it recorded in 
the db as well.

Stream from registered models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Register your models in settings.py with the stream enabled:

::

   MQUEUE_AUTOREGISTER = (
   	#('app.module.model', registration level: 1=create+delete, 2=1+save, True to enable the live stream),
   	('alapage.models.Page', 2, True),
   	('contactform.models.Email', 1, True),
   	)

In this example the Page model will send messages in the admin channel everytime it is created/saved/deleted. The contact
form will fire a message everytime an Email is created/deleted.

Direct broadcast of events
~~~~~~~~~~~~~~~~~~~~~~~~~~

Got to /mq/ as superuser and use the form to broadcast a message to any channel.

By default the sent messages popup on the top-right corner of the page. The next section will describe how to 
customize the handlers on the client side according to the event class.
