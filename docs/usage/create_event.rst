Record events
=============

You can plug mqueue into your app by creating an event whenever you
need. It can be in the save method of a model, a form\_valid method of a
view or in a signal for example.

Event creation
~~~~~~~~~~~~~~

.. highlight:: python

::

   from mqueue.models import MEvent 
   from myapp.models import MyModel

   # simpliest event
   MEvent.objects.create(name = 'Something happened!')
   
   # full event
   MEvent.objects.create( 
      name = obj.title, 
      model = MyModel, 
      obj_pk =obj.pk, 
      instance = obj, 
      user = request.user, 
      url ='/anything/'+obj.slug+'/', 
      admin_url ='/admin/app/model/'+str(obj.pk)+'/', 
      notes = 'Object X was saved!',
      event_class = 'Info',
      request = request,
      bucket = "bucket_name",
      data = {"foo": "bar"},
      scope = "users",
      groups = [group1] # a list of django group objects
      )

The only required field is ``name``

The ``instance`` parameter will not be recorded: it is only used for
auto guessing some fields. 

The ``scope`` parameter is used by the Api to query the database. Possible values are: ``public``, ``users``, ``staff``
and ``superuser`` (default). It controls who can view an event in the Api.

Note this method will return the event instance just created. There is an option for not to save it immediately:

::

   from mqueue.models import MEvent 
   from myapp.models import MyModel

   # initiate event
   mevent = MEvent.objects.create(name='No commit', commit=False)
   # do things ...
   # update event
   mevent.notes='Some stuff'
   # and save it
   mevent.save()
   

Fields autoguess
~~~~~~~~~~~~~~~~

If you provided an instance or a content\_type and a model mqueue will
guess the following fields unless you provided arguments for:

-  ``user``: checks if you model has a ``user`` field or an ``editor``
   field and populates from it
-  ``url``: checks for a ``get_event_object_url()`` method in your
   model, and then check for a ``get_absolute_url()`` method and
   populates from it. Write your own ``get_event_object_url()`` method  in your model to 
   manage which url will be associated to the object.
-  ``admin_url``: will be reversed from the instance

Example:

::

   from mqueue.models import MEvent

   MEvent.objects.create(name = 'Something happened!', instance=my_obj)


So that ``user``, ``url`` and ``admin_url`` will be auto guessed
