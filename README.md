# Django Mqueue

Events queue application for Django. Features:

- **Monitor models**: models can be registered to autogenerate events on create/update/delete actions
- **Export events**: save events to Redis or send them over websockets

:books: Read the [documentation](http://synw.github.io/django-mqueue/)

Example:

   ```python
   MEvent.objects.create(name="Test event", event_class="test", data={"k":"v"})
   ```

Events can be linked to a model instance and a user instance.

![Event queue screenshot](https://raw.github.com/synw/django-mqueue/master/docs/_static/events_list.png)

## Real time events demo

A websockets demo: [django-mqueue-livefeed](https://github.com/synw/django-mqueue-livefeed) is available

## Documentation

 - [Get started](http://synw.github.io/django-mqueue/get_started)
    - [Install](http://synw.github.io/django-mqueue/get_started/install)
    - [Basics](http://synw.github.io/django-mqueue/get_started/basics)
 - [Events](http://synw.github.io/django-mqueue/events)
    - [Parameters](http://synw.github.io/django-mqueue/events/parameters)
    - [Fields autoguess](http://synw.github.io/django-mqueue/events/fields_autoguess)
    - [Query events](http://synw.github.io/django-mqueue/events/query_events)
 - [Model events](http://synw.github.io/django-mqueue/model_events)
    - [Registered models](http://synw.github.io/django-mqueue/model_events/registered_models)
    - [Watchers](http://synw.github.io/django-mqueue/model_events/watchers)
 - [Post processing](http://synw.github.io/django-mqueue/post_processing)
    - [Model callbacks](http://synw.github.io/django-mqueue/post_processing/model_callbacks)
    - [Hooks](http://synw.github.io/django-mqueue/post_processing/hooks)
     - [Hooks](http://synw.github.io/django-mqueue/post_processing/hooks)
        - [Redis](http://synw.github.io/django-mqueue/post_processing/hooks/redis)
        - [Centrifugo](http://synw.github.io/django-mqueue/post_processing/hooks/centrifugo)
        - [Custom](http://synw.github.io/django-mqueue/post_processing/hooks/custom)
 - [Extra](http://synw.github.io/django-mqueue/extra)
    - [Livefeed](http://synw.github.io/django-mqueue/extra/livefeed)
    - [Logs handler](http://synw.github.io/django-mqueue/extra/logs_handler)
    - [Graphical settings](http://synw.github.io/django-mqueue/extra/graphical_settings)
