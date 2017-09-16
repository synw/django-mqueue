# Django Mqueue

[![Build Status](https://travis-ci.org/synw/django-mqueue.svg?branch=master)](https://travis-ci.org/synw/django-mqueue)

Events queue application for Django. Features:

- **Monitor models**: models can be registered to autogenerate events on create/update/delete actions
- **Handle logs**: the logs will be saved in the database as events or exported
- **Export events**: save events to Postgresql, Influxdb, Redis or send them over websockets.
- **Query events** from the frontend - *New in 0.9*: a Graphql api to retrieve events

Example:

   ```pyhton
   MEvent.objects.create(name="Test event", event_class="test", data={"k":"v"})
   ```

Events can be linked to a model instance and a user instance.

Check the [documentation](http://django-mqueue.readthedocs.org/en/latest/)

![Event queue screenshot](https://raw.github.com/synw/django-mqueue/master/docs/_static/events_list.png)

### Admin interface

Note: to run the tests you will need [django-fake-model](https://github.com/erm0l0v/django-fake-model)

### Events dashboard

Dashboard with [django-chartflo](https://github.com/synw/django-chartflo):

![Event dashboard](https://raw.github.com/synw/django-mqueue/master/docs/_static/events_dashboard.png)
