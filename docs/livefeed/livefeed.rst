Livefeed
========

A view and template are available to display the events in real time using Alpinejs on the frontend

Install and configure `django-instant <https://github.com/synw/django-instant>`_ for
the websockets

Quickstart
----------

Use the installer to quickly have a local websockets server: `instructions <https://github.com/synw/django-instant#quick-start>`_

Then use the builtin template or customize it: `templates/mqueue/livefeed/index.html`. See 
an `example <https://github.com/synw/django-mqueue-livefeed/blob/master/livefeed/templates/livefeed.html>`_

Add to urls:

 .. highlight:: python

::

   path("livefeed/", TemplateView.as_view(template_name="mqueue/livefeed/index.html")),

Example
-------

An `example project <https://github.com/synw/django-mqueue-livefeed>`_ is available