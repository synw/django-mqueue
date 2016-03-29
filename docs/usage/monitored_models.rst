Monitored Models
================

.. highlight:: python

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

``ObjectLevelMonitoredModel`` : this one needs a migration as it adds a``monitoring_level`` 
field to the model. Any instance can be set to a
monitoring level via the value of this field: ``0`` is no monitoring
(default), ``1`` records create and delete, ``2`` records also saves.

Switch off model monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If later on you want to switch off monitoring for some models
add a setting ``MQUEUE_STOP_MONITORING`` with the class names of the
models:

::

   python MQUEUE_STOP_MONITORING = ['Model1', 'Model2']
