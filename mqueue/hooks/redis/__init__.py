# -*- coding: utf-8 -*-

import time
from typing import Dict

from mqueue.conf import DOMAIN
from mqueue.hooks.redis import serializer
from mqueue.conf import HOOKS
from mqueue.models import MEvent


try:
    import redis

    conf = HOOKS["redis"]
    R = redis.StrictRedis(  # type: ignore
        host=conf["host"], port=conf["port"], db=conf["db"]
    )
    EVENT_NUM = int(time.time())
except ImportError:
    pass


def save(event: MEvent, conf: Dict[str, str]):
    global EVENT_NUM
    global R
    name = DOMAIN + "_event" + str(EVENT_NUM)
    data = serializer.Pack(event)
    R.set(name, data)
    EVENT_NUM += 1
