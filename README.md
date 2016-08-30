# Django Mqueue

[![Build Status](https://travis-ci.org/synw/django-mqueue.svg?branch=master)](https://travis-ci.org/synw/django-mqueue)

Events queue application for Django: can be used for monitoring or loging, or to build apps with moderation.
Features:

- Send events from code: they will be recorder into the db
- Monitoring on models: the events (create/save/delete) will be recorder according to the choosen log level
- Logs handler: to record the Django logs into the db
- Experimental feature: live stream of events on websockets with 
[Centrifugo](https://github.com/centrifugal/centrifugo/), using 
[Django Instant](https://github.com/synw/django-instant).

Events can be linked to a model instance and a user instance.

Check the [documentation](http://django-mqueue.readthedocs.org/en/latest/)

![Event queue screenshot](https://raw.github.com/synw/django-mqueue/master/docs/img/events_list.png)
 