from django.conf import settings
from ...conf import DOMAIN
try:
    from instant.conf import SITE_SLUG
    from instant.producers import publish
except ImportError:
    pass


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
    site = SITE_SLUG
    if "site" in event.data:
        site = event.data["site"]
    err = publish(
        conf["channel"],
        event.name,
        event_class=event.event_class,
        data=data,
        site=site,
    )
    if err is not None:
        if settings.DEBUG:
            print("Error in Centrifugo mqueue hook:", err)
        raise Exception(err)
