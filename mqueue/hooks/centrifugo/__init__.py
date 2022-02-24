from typing import Any, Dict
from django.conf import settings

from mqueue.models import MEvent

# from ...conf import DOMAIN
try:
    from instant.conf import SITE_SLUG
    from instant.producers import publish
except ImportError:
    pass


def save(event: MEvent, conf: Dict[str, Any]):
    data: Dict[str, Any] = {}
    if event.data:
        data["data"] = event.data
    user = "anonymous"
    if event.user:
        user = event.user.username  # type: ignore
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
    site = SITE_SLUG
    if "site" in event.data:  # type: ignore
        site = event.data["site"]  # type: ignore
    try:
        publish(
            conf["channel"],
            event.name,
            event_class=event.event_class,
            data=data,
            bucket=bucket,
            site=site,
        )
    except Exception as err:
        if settings.DEBUG:
            print("Error in Centrifugo mqueue hook:", err)
        raise Exception(err)
