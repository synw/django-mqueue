from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from mqueue.models import MEvent
from mqueue.utils import get_url, get_admin_url, get_object_name
from mqueue.conf import WATCH, LIVE_FEED
if LIVE_FEED is True:
    from mqueue_livefeed.conf import CHANNEL, EXTRA_CHANNELS, STREAM_MODELS, SITE_NAME
    from instant.producers import publish


def send_msg(objclass, instance, event_str):
    obj_name = get_object_name(instance, instance)
    # try to get the admin url
    admin_url = get_admin_url(instance)
    event_class = instance.__class__.__name__ +" "+event_str
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
    if LIVE_FEED is True and STREAM_MODELS is True:
        data = {"admin_url": admin_url, "site": SITE_NAME}
        publish(message=obj_name, event_class=event_class, channel=CHANNEL, data=data)
        if len(EXTRA_CHANNELS) > 0:
            for channel in EXTRA_CHANNELS:
                publish(message=obj_name, event_class=event_class, channel=channel, data=data)
    return

def logout_action(sender, user, **kwargs):
    send_msg(sender, user, "logout") 
    
def login_action(sender, user, **kwargs):
    send_msg(sender, user, "login")

def login_failed(sender, credentials, **kwargs):
    # create event
    name = "Login failed"
    event_class = "Warning"
    MEvent.objects.create(
        name=name,
        event_class=event_class,
        notes = credentials
    )
    if LIVE_FEED is True and STREAM_MODELS is True:
        data = {"site": SITE_NAME, "username": credentials["username"]}
        publish(message=name, event_class=event_class, channel=CHANNEL, data=data)
        if len(EXTRA_CHANNELS) > 0:
            for channel in EXTRA_CHANNELS:
                publish(message=name, event_class=event_class, channel=channel, data=data)
    return

def init_watchers(w):
    print("WATCHERS:", w)
    for w in WATCH:
        if w == "login":
            print("LOGIN")
            user_logged_in.connect(login_action)
        elif w == "logout":
            user_logged_out.connect(logout_action)
        elif w == "login_failed":
            user_login_failed.connect(login_failed)
    return
    