Record events
=============

.. highlight:: python

You can plug mqueue into your app by creating a mevent whenever you
need. It can be in the save method of a model, a form\_valid method of a
view or in a signal for example.

Event creation
~~~~~~~~~~~~~~

::

   python from mqueue.models import MEvent from myapp.models import MyModel

   # simpliest event
   MEvent.objects.create(name = 'Something happened!')
   
   # full event
   MEvent.objects.create( 
      name = obj.title, 
      model = MyModel, obj_pk =
      obj.pk, 
      instance = obj, 
      user = request.user, 
      url ='/anything/'+obj.slug+'/', 
      admin_url ='/admin/app/model/'+str(obj.pk)+'/', 
      notes = 'Object X was saved!',
      event_class = 'Info' 
      )

The only required field is ``name``

The ``instance`` parameter will not be recorded: it is only used for
auto guessing some fields.

Fields autoguess
~~~~~~~~~~~~~~~~

If you provided an instance or a content\_type and a model mqueue will
guess the following fields unless you provided arguments for:

-  ``user``: checks if you model has a ``user`` field or an ``editor``
   field and populates from it
-  ``url``: checks for a ``get_event_object_url()`` method in your
   model, and then check for a ``get_absolute_url()`` method and
   populates from it
-  ``admin_url``: will be reversed from the instance

Example:

::

   python from mqueue.models import MEvent

   MEvent.objects.create(name = 'Something happened!', instance=my_obj)


So that ``user``, ``url`` and ``admin_url`` will be auto guessed
