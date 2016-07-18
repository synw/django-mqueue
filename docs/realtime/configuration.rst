Configuration
=============

Mqueue can deliver the messages in real time to the users. This is made using the websockets.

**Warning**: this feature is experimental and is not yet in the pip version (use master). The api may change.

You must have Redis and Nodejs installed. On Debian and friends: ``sudo apt-get install redis-server nodejs``

Then ``pip install redis`` to get the python client

Enable the mqueue views by adding this to your urls.py:

.. highlight:: python

::

   url('^mq/', include('mqueue.urls')),

Settings
~~~~~~~~

In settings.py:

::
   
   # 1. Required settings
   MQUEUE_LIVE_STREAM = True
   SITE_SLUG = 'my_site_name'
   SITE_NAME = 'My site name'
   
   # 2. Optional settings
   MQUEUE_GLOBAL_STREAMS = ('admin',)
   # set Redis config: default is:
   MQUEUE_REDIS_HOST = 'localhost'
   MQUEUE_REDIS_PORT = 6379
   MQUEUE_REDIS_DB = 0
   # set the websocket server config. Default is:
   WSOCK_HOST = 'localhost'
   WSOCK_PORT = 3000

By default the channels will be prefixed with the site name. If you want one channel to be able to receive messages from 
several sites enable it as global in MQUEUE_GLOBAL_STREAMS. Example here: the admin channel will receive messages from 
all the sites it is connected to: if you enabled the log handler the logs will automatically be broadcasted to the admin 
channel. And if this one is global the admin can see the logs from all the connected sites in his live stream. 

Important: if you use the log handler these settings must be placed before ``from mqueue.conf import LOGGING``
