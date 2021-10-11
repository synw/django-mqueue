# Django Mqueue

Events queue application for Django. Features:

- **Monitor models**: models can be registered to autogenerate events on create/update/delete actions
- **Query events** from the frontend: a Graphql api is available to retrieve events
- **Export events**: save events to Redis or send them over websockets
- **Handle logs**: the logs will be saved in the database as events or exported

Example:

   ```python
   MEvent.objects.create(name="Test event", event_class="test", data={"k":"v"})
   ```

Events can be linked to a model instance and a user instance.

Check the [documentation](http://django-mqueue.readthedocs.org/en/latest/)

![Event queue screenshot](https://raw.github.com/synw/django-mqueue/master/docs/_static/events_list.png)

## Websockets events demo

Push events to websockets demo: [django-mqueue-livefeed](https://github.com/synw/django-mqueue-livefeed)
