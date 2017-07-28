Graphical settings
==================

Event classes
~~~~~~~~~~~~~

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

.. figure:: /_static/events_list.png
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

Event Extra html
~~~~~~~~~~~~~~~~

You can add some extra html that will display after the event\_class
label:

::

   EVENT_EXTRA_HTML = {                  
	   #~ 'Event class label' : 'html to apply',                 
	   'My event' : ' <blink>!!</blink>',                 
	   }

Event Icons
~~~~~~~~~~~

You can provide html to display icons in your ``event_class``. The
defaults are the font-awesome ones (embeded in mqueue):

::

   EVENT_ICONS_HTML = {                  
   	#~ 'Event class label' : 'icon html',                 
   	'Default' : '<i class="fa fa-flash"></i>',
   	'Important' : '<i class="fa fa-exclamation"></i>',
   	'Ok' : '<i class="fa fa-thumbs-up"></i>',
   	'Info' : '<i class="fa fa-info-circle"></i>',
   	'Debug' : '<i class="fa fa-cog"></i>',
   	'Warning' : '<i class="fa fa-exclamation"></i>',
   	'Error' : '<i class="fa fa-exclamation-triangle"></i>',
   	'Object edited' : '<i class="fa fa-pencil"></i>',
   	'Object created' : '<i class="fa fa-plus"></i>',
   	'Object deleted' : '<i class="fa fa-remove"></i>',               
   	}

If you don't want any icons set it empty.
