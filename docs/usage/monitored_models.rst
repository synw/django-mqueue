Monitored Models
================

.. highlight:: python

Enable model monitoring
^^^^^^^^^^^^^^^^^^^^^^^

Basic monitoring
~~~~~~~~~~~~~~~~

If you want a model to be automaticaly monitored you can inherit from
these base models that create events via signals for all the inherited
monitored models.

``MonitoredModel`` : records any instance creation and deletion:

::

   python from mqueue.models import MonitoredModel

   #for an existing model replace class MyModel(models.Model) by this:
   class MyModel(MonitoredModel): 
      # ...

To record also every save of a model instance replace ``MonitoredModel``
by ``HighlyMonitoredModel``.

Note: for these no migration is needed for an existing model,
just plug and play.

Object level monitoring
~~~~~~~~~~~~~~~~~~~~~~~

``ObjectLevelMonitoredModel`` : this one needs a migration as it adds a ``monitoring_level`` 
field to the model. Any instance can be set to a
monitoring level via the value of this field: ``0`` is no monitoring
(default), ``1`` records create and delete, ``2`` records also saves. 

Ex: let's say you have a page management app and you want to monitor only certain pages:

::

   # models.py
   python from mqueue.models import MonitoredModel

   class Page(ObjectLevelMonitoredModel): 
      # ...
      
   # admin.py
   from django.contrib import admin
   
   @admin.register(Page)
   class PageAdmin(admin.ModelAdmin):
   	# ...
   	def get_fieldsets(self, request, obj=None):
   		fieldsets = super(PageAdmin, self).get_fieldsets(request, obj)
   		#~ if we want only the superusers to be able to see the monitoring field in admin
   		if request.user.is_superuser:
   			fieldsets += ( 'Monitoring', {'fields': ('monitoring_level',)} ),
   		return fieldsets

Switch off model monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If later on you want to switch off monitoring for some models
add a setting ``MQUEUE_STOP_MONITORING`` with the class names of the
models:

::
   
   # settings.py
   MQUEUE_STOP_MONITORING = ['Model1', 'Model2']
