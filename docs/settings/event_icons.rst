Event Icons
^^^^^^^^^^^

.. highlight:: python

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
