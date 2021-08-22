from .models import MEvent
from .utils import get_user, get_url, get_admin_url, get_object_name


def mmessage_create(sender, instance, created, **kwargs):
    if created is True:
        # try to get the user
        user = get_user(instance)
        # try to get the object name
        obj_name = get_object_name(instance, user)
        # try to get the admin url
        admin_url = get_admin_url(instance)
        event_class = instance.__class__.__name__ + " created"
        has_event_method = getattr(instance, "event", None)
        # create event
        evt = MEvent.objects.create(
            model=instance.__class__,
            name=obj_name,
            obj_pk=instance.pk,
            user=user,
            url=get_url(instance),
            admin_url=admin_url,
            event_class=event_class,
            commit=not has_event_method,
        )
        if has_event_method:
            evt = instance.event(evt, "create")
            evt.save()
    return


def mmessage_delete(sender, instance, **kwargs):
    # try to get the user
    user = get_user(instance)
    # try to get the object name
    obj_name = get_object_name(instance, user)
    event_class = instance.__class__.__name__ + " deleted"
    has_event_method = getattr(instance, "event", None)
    # create event
    evt = MEvent.objects.create(
        model=instance.__class__,
        name=obj_name,
        obj_pk=instance.pk,
        user=user,
        event_class=event_class,
        commit=not has_event_method,
    )
    if has_event_method:
        evt = instance.event(evt, "delete")
        evt.save()
    return


def mmessage_update(sender, instance, created, **kwargs):
    if created is False:
        # try to get the user
        user = get_user(instance)
        if "name" not in kwargs.keys():
            # try to get the object name
            obj_name = get_object_name(instance, user)
        else:
            obj_name = kwargs("name")
        # try to get the admin url
        admin_url = get_admin_url(instance)
        event_str = " edited"
        has_event_method = getattr(instance, "event", None)
        event_class = instance.__class__.__name__ + event_str
        # create event
        evt = MEvent.objects.create(
            model=instance.__class__,
            name=obj_name,
            obj_pk=instance.pk,
            user=user,
            url=get_url(instance),
            admin_url=admin_url,
            event_class=event_class,
            commit=not has_event_method,
        )
        if has_event_method:
            evt = instance.event(evt, "update")
            evt.save()
    return
