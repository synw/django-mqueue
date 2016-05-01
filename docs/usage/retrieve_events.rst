Retrieve events
=============

Events for a model:

.. highlight:: python

::

   from mqueue.models import MEvent
   from myapp.models import MyModel
   
   # get all events for the model
   events_for_mymodel = MEvents.objects.get_for_model(MyModel)
   
   # count all events for the model
   events_for_mymodel = MEvents.objects.count_for_model(MyModel)

Events for an object:

.. highlight:: python

::

   from mqueue.models import MEvent
   
   # get all events for the model
   events_for_myobject = MEvents.objects.get_for_object(any_model_instance)