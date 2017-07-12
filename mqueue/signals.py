from __future__ import print_function
from mqueue.models import MEvent
from mqueue.utils import get_user, get_url, get_admin_url, get_object_name


def mmessage_create(sender, instance, created, **kwargs):
    if created:
        # try to get the user
        user = get_user(instance)
        # try to get the object name
        obj_name = get_object_name(instance, user)
        # try to get the admin url
        admin_url = get_admin_url(instance)
        event_class = instance.__class__.__name__ + ' created'
        # create event
        MEvent.objects.create(
            model=instance.__class__,
            name=obj_name,
            obj_pk=instance.pk,
            user=user,
            url=get_url(instance),
            admin_url=admin_url,
            event_class=event_class,
        )
    return


def mmessage_delete(sender, instance, **kwargs):
    # try to get the user
    user = get_user(instance)
    # try to get the object name
    obj_name = get_object_name(instance, user)
    event_class = instance.__class__.__name__ + ' deleted'
    # create event
    MEvent.objects.create(
        model=instance.__class__,
        name=obj_name,
        obj_pk=instance.pk,
        user=user,
        event_class=event_class,
    )
    return


def mmessage_save(sender, instance, created, **kwargs):
    # try to get the user
    user = get_user(instance)
    if 'name' not in kwargs.keys():
        # try to get the object name
        obj_name = get_object_name(instance, user)
    else:
        obj_name = kwargs('name')
    # try to get the admin url
    admin_url = get_admin_url(instance)
    event_str = ' edited'
    if created:
        event_str = ' created'
    event_class = instance.__class__.__name__ + event_str
    # create event
    MEvent.objects.create(
        model=instance.__class__,
        name=obj_name,
        obj_pk=instance.pk,
        user=user,
        url=get_url(instance),
        admin_url=admin_url,
        event_class=event_class,
    )
    return
