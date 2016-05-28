Event classes
^^^^^^^^^^^^^

You can define your custom set of event classes and the corresponding
css classes to display in the admin. The default values are (check ``mqueue/static/mqueue.css``):

.. highlight:: python

::

   MQUEUE_EVENT_CLASSES = {                  
	#~ 'Event class label' : 'css class to apply',                
	'Default' : 'mq-label mq-default',
   	'Important' : 'mq-label mq-important',
   	'Ok' : 'mq-label mq-ok',
   	'Info' : 'mq-label mq-info',
   	'Debug' : 'mq-label mq-debug',
   	'Warning' : 'mq-label mq-warning',
   	'Error' : 'mq-label mq-error',
   	'Object created' : 'mq-label mq-created',
   	'Object edited' : 'mq-label mq-edited',
   	'Object deleted' : 'mq-label mq-deleted',                
	}

Note: if the ``event_class`` field value is not in
MQUEUE\_EVENT\_CLASSES, the display will fallback to 'Default'.

.. figure:: /img/events_list.png
   :alt: Event classes

To use your own event classes set a ``MQUEUE_EVENT_CLASSES`` setting.
Ex:

::

   MQUEUE_EVENT_CLASSES = {                
   #~ 'Event class label' : 'css class to apply',
   'Default' : 'mydefaultcssclass',
   'User registered' : 'mycssclass',
   'Post reviewed' : 'mycssclass mycssclass2',
   'Error in some process' : 'mycssclass mycssclass2',
   # ...                 
   }
