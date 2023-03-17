# Django Mqueue

Events queue application for Django. Features:

- **Monitor models**: models can be registered to autogenerate events on create/update/delete actions
- **Export events**: save events to Redis or send them over websockets

:books: Read the [documentation](https://synw.github.io/django-mqueue/)

Example:

   ```python
   MEvent.objects.create(name="Test event", event_class="test", data={"k":"v"})
   ```

Events can be linked to a model instance and a user instance.

![Event queue screenshot](https://raw.github.com/synw/django-mqueue/master/docsite/src/assets/screenshot.png)

## Real time events demo

A websockets demo: [django-mqueue-livefeed](https://github.com/synw/django-mqueue-livefeed) is available

## Documentation

 - [Get started](https://synw.github.io/django-mqueue/get_started)
    - [Install](https://synw.github.io/django-mqueue/get_started/install)
    - [Basics](https://synw.github.io/django-mqueue/get_started/basics)
 - [Events](https://synw.github.io/django-mqueue/events)
    - [Parameters](https://synw.github.io/django-mqueue/events/parameters)
    - [Fields autoguess](https://synw.github.io/django-mqueue/events/fields_autoguess)
    - [Query events](https://synw.github.io/django-mqueue/events/query_events)
 - [Model events](https://synw.github.io/django-mqueue/model_events)
    - [Registered models](https://synw.github.io/django-mqueue/model_events/registered_models)
    - [Watchers](https://synw.github.io/django-mqueue/model_events/watchers)
 - [Post processing](https://synw.github.io/django-mqueue/post_processing)
    - [Model callbacks](https://synw.github.io/django-mqueue/post_processing/model_callbacks)
    - [Hooks](https://synw.github.io/django-mqueue/post_processing/hooks)
     - [Hooks](https://synw.github.io/django-mqueue/post_processing/hooks)
        - [Redis](https://synw.github.io/django-mqueue/post_processing/hooks/redis)
        - [Centrifugo](https://synw.github.io/django-mqueue/post_processing/hooks/centrifugo)
        - [Custom](https://synw.github.io/django-mqueue/post_processing/hooks/custom)
 - [Extra](https://synw.github.io/django-mqueue/extra)
    - [Livefeed](https://synw.github.io/django-mqueue/extra/livefeed)
    - [Logs handler](https://synw.github.io/django-mqueue/extra/logs_handler)
    - [Graphical settings](https://synw.github.io/django-mqueue/extra/graphical_settings)
