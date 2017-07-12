Hooks
=====

*New in 0.7.1* (inspired by `Logrus <https://github.com/sirupsen/logrus>`_)

Optional hooks can be used to perform extra actions on events. Available hooks:

- **Postgresql**: a Go program that records the events in a postgresql database
- **Influxdb**: a Go program that records the events in an influxdb database
- **Redis**: record the events in Redis

Postgresql
----------

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
   
Influxdb
--------

::

   "influxdb": {
        "path": "mqueue.hooks.influxdb",
        "addr": "localhost:8086",
        "user": "admin",
        "password": "admin",
        "database": "events"
    }

Create the database in Influxdb

Redis
-----

::

   "redis": {
        "path": "mqueue.hooks.redis",
        "host": "localhost",
        "port": 6379,
        "db": 0,
    }
    

   
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

Create a ``save`` function in your hook that takes and event object as parameter and the hook config. Example:

::

   def save(event, conf):
       print(event, conf["myparam"])
