from django.conf import settings
from instant.producers import publish
from mqueue.conf import DOMAIN


def save(event, conf):
    data = {}
    if event.data:
        data = event.data
    user = "anonymous"
    if event.user:
        user = event.user.username
    url = ""
    if event.url:
        url = event.url
    bucket = ""
    if event.bucket:
        bucket = event.bucket
    admin_url = ""
    if event.admin_url:
        admin_url = event.admin_url
    data["user"] = user
    data["url"] = url
    data["admin_url"] = admin_url
    data["bucket"] = bucket
    err = publish(
        message=event.name, 
        event_class=event.event_class,
        channel = conf["channel"], 
        data = data
    )
    if err is not None:
        if settings.DEBUG:
            print("Error in Centrifugo mqueue hook:", err)