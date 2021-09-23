from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from .models import MEvent
from .utils import get_url, get_admin_url, get_object_name
from .conf import WATCH


def send_msg(objclass, instance, event_str):
    obj_name = get_object_name(instance, instance)
    # try to get the admin url
    admin_url = get_admin_url(instance)
    event_class = instance.__class__.__name__ + " " + event_str
    # create event
    MEvent.objects.create(
        model=instance.__class__,
        name=obj_name,
        obj_pk=instance.pk,
        user=instance,
        url=get_url(instance),
        admin_url=admin_url,
        event_class=event_class,
    )
    return


def logout_action(sender, user, **kwargs):
    send_msg(sender, user, "logout")


def login_action(sender, user, **kwargs):
    send_msg(sender, user, "login")


def login_failed(sender, credentials, **kwargs):
    # create event
    name = "Login failed"
    event_class = "Warning"
    MEvent.objects.create(name=name, event_class=event_class, notes=credentials)
    return


def init_watchers(w):
    for w in WATCH:
        if w == "login":
            user_logged_in.connect(login_action)
        elif w == "logout":
            user_logged_out.connect(logout_action)
        elif w == "login_failed":
            user_login_failed.connect(login_failed)
    return
