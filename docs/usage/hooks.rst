Hooks
=====

Optional hooks can be used to perform extra actions on events (inspired by `Logrus <https://github.com/sirupsen/logrus>`_). 
Available hooks:

- **Redis**: record the events in Redis (python)
- **Centrifugo**: push events as messages in the Centrifugo websockets server (python)

Redis
-----

::

   MQUEUE_HOOKS = {
    "redis": {
            "path": "mqueue.hooks.redis",
            "host": "localhost",
            "port": 6379,
            "db": 0,
        }
    }

Centrifugo
----------

Install `Django Instant <https://github.com/synw/django-instant>`_ to manage the websockets

::


   MQUEUE_HOOKS = {
        "centrifugo": {
            "path": "mqueue.hooks.centrifugo",
            "channel": "$events"
        }
   }
   
Custom hook
-----------

Create a file : ``mymodule/mqueue_hook.py``

Declare your hook and config in settings:

::

   MQUEUE_HOOKS = {
    "myhook": {
        "path": "mymodule.mqueue_hook",
        "myparam": "myvalue",
    }
   }

Create a ``save`` function in your hook that takes and event object as parameter and the hook config. Example:

::

   def save(event, conf):
       print(event, conf["myparam"])
