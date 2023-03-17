# Django Mqueue

Events queue application for Django. Features:

- **Monitor models**: models can be registered to autogenerate events on create/update/delete actions
- **Export events**: save events to Redis or send them over websockets

:books: Read the [documentation](/)

Example:

   ```python
   MEvent.objects.create(name="Test event", event_class="test", data={"k":"v"})
   ```

Events can be linked to a model instance and a user instance.

![Event queue screenshot](https://raw.github.com/synw/django-mqueue/master/docsite/src/assets/screenshot.png)

## Real time events demo

A websockets demo: [django-mqueue-livefeed](https://github.com/synw/django-mqueue-livefeed) is available

## Documentation

 - [Get started](/get_started)
    - [Install](/get_started/install)
    - [Basics](/get_started/basics)
 - [Events](/events)
    - [Parameters](/events/parameters)
    - [Fields autoguess](/events/fields_autoguess)
    - [Query events](/events/query_events)
 - [Model events](/model_events)
    - [Registered models](/model_events/registered_models)
    - [Watchers](/model_events/watchers)
 - [Post processing](/post_processing)
    - [Model callbacks](/post_processing/model_callbacks)
    - [Hooks](/post_processing/hooks)
     - [Hooks](/post_processing/hooks)
        - [Redis](/post_processing/hooks/redis)
        - [Centrifugo](/post_processing/hooks/centrifugo)
        - [Custom](/post_processing/hooks/custom)
 - [Extra](/extra)
    - [Livefeed](/extra/livefeed)
    - [Logs handler](/extra/logs_handler)
    - [Graphical settings](/extra/graphical_settings)
