Event Icons
^^^^^^^^^^^

.. highlight:: python

You can provide html for displaying icons in your ``event_class``. The
defaults are:

::

   python EVENT_ICONS_HTML = {                  
	#~ 'Event class label' : 'icon html',                 
	'Default' : '<span class="glyphicon glyphicon-flash"></span>',                 
	'Important' : '<span class="glyphicon glyphicon-star"></span>',                 
	'Ok' : '<span class="glyphicon glyphicon-ok"></span>',                 
	'Info' : '<span class="glyphicon glyphicon-hand-right"></span>',                 
	'Debug' : '<span class="glyphicon glyphicon-cog"></span>',                 
	'Warning' : '<span class="glyphicon glyphicon-exclamation-sign"></span>',                 
	'Error' : '<span class="glyphicon glyphicon-alert"></span>',                 
	'Object edited' : '<span class="glyphicon glyphicon-pencil"></span>',                 
	'Object created' : '<span class="glyphicon glyphicon-download-alt"></span>',                 
	'Object deleted' : '<span class="glyphicon glyphicon-remove"></span>',                 
	}

If you don't want any icons set it empty.
