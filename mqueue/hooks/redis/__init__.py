# -*- coding: utf-8 -*-

import time
from mqueue.conf import DOMAIN
from mqueue.hooks.redis import serializer
from mqueue.conf import HOOKS


try:
    import redis

    conf = HOOKS["redis"]
    R = redis.StrictRedis(host=conf["host"], port=conf["port"], db=conf["db"])
    EVENT_NUM = int(time.time())
except Exception:
    pass


def save(event, conf):
    global EVENT_NUM
    global R
    name = DOMAIN + "_event" + str(EVENT_NUM)
    event.request = event.request.replace("\n", "//")
    data = serializer.Pack(event)
    R.set(name, data)
    EVENT_NUM += 1
