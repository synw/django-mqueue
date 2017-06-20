Hooks
=====

*New in 0.7.1* (inspired by `Logrus <https://github.com/sirupsen/logrus>`_)

Optional hooks can be used to perform extra actions on events.

Available hooks
---------------

**Postgresql**: a Go program that records the events in a postgresql database
**Influxdb**: a Go program that records the events in an influxdb database

Usage
-----

In ``settings.py``

.. highlight:: python

::

   MQUEUE_HOOKS = {
    "postgresql": {
        "path": "mqueue.hooks.postgresql",
        "addr": "localhost",
        "user": "user",
        "password": "pwd",
        "database": "mydomain_events",
        "table": "events"
    }
   }

Create the database in postgresql and migrate it with a management command:

::

   python3 manage.py mqueue_migrate_pg
   
Note: for the Go based hooks you might need to make the binary (``mqueue/hooks/<hookname>/run``) executable with chmod
   
Custom hook
-----------

Create a file : ``mymodule.mqueue_hook.py``

Declare your hook and config in settings:

::

   MQUEUE_HOOKS = {
    "myhook": {
        "path": "mymodule.mqueue_hook.py",
        "myparam": "myvalue",
    }
   }

Create a ``Save`` function in your hook that takes and event object as parameter and the hook config. Example:

::

   def Save(event, hook):
       print(event, hook["myparam"])
