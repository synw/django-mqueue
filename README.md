# Django Mqueue

[![Build Status](https://travis-ci.org/synw/django-mqueue.svg?branch=master)](https://travis-ci.org/synw/django-mqueue)

Events queue application for Django: can be used for moderation or monitoring or loging.
Events can be linked to a model instance and a user instance. This app is pluggable on existing models to
enable monitoring on them. It also provides a log handler to store the django logs in the db.

Read the [documentation](http://django-mqueue.readthedocs.org/en/latest/)

![Event queue screenshot](https://raw.github.com/synw/django-mqueue/master/docs/img/events_list.png)
 