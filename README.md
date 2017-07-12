# Django Mqueue

[![Build Status](https://travis-ci.org/synw/django-mqueue.svg?branch=master)](https://travis-ci.org/synw/django-mqueue)

Events queue application for Django. Can be used for monitoring or loging, or to build any events-based app.
Features:

- Send events from code: they will be recorded into the db
- Monitoring on models: the events (create/update/delete) will be recorded according to the choosen log level
- Logs handler: to record the Django logs into the db
- Hooks: save the event to another database, push it to websockets or use a custom action

Events can be linked to a model instance and a user instance.

Check the [documentation](http://django-mqueue.readthedocs.org/en/latest/)

![Event queue screenshot](https://raw.github.com/synw/django-mqueue/master/docs/_static/events_list.png)

Note: to run the tests you will need [django-fake-model](https://github.com/erm0l0v/django-fake-model)
