Hooks
=====

Optional hooks can be used to perform extra actions on events (inspired by `Logrus <https://github.com/sirupsen/logrus>`_). 
Available hooks:

- **Redis**: record the events in Redis (python)
- **Centrifugo**: push events as messages in the Centrifugo websockets server (python)

Redis
-----

::

   "redis": {
        "path": "mqueue.hooks.redis",
        "host": "localhost",
        "port": 6379,
        "db": 0,
    }

Centrifugo
----------

Install `Django Instant <https://github.com/synw/django-instant>`_ to manage the websockets

::

   "centrifugo": {
        "path": "mqueue.hooks.centrifugo",
        "channel": "$events"
    }  

   
Note: for the Go based hooks you might need to make the binary (``mqueue/hooks/<hookname>/run``) executable with chmod
   
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
