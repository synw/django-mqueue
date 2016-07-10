# -*- coding: utf-8 -*-

import random
from django import template
from django.conf import settings


def generate_key():
    return ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(60)])


LIVE_STREAM = getattr(settings, 'MQUEUE_LIVE_STREAM', False)
if LIVE_STREAM is True:
    import redis
    REDIS_HOST = getattr(settings, 'MQUEUE_REDIS_HOST', 'localhost')
    REDIS_PORT = getattr(settings, 'MQUEUE_REDIS_PORT', 6379)
    REDIS_DB = getattr(settings, 'MQUEUE_REDIS_DB', 0)
    WSOCK_HOST = getattr(settings, 'MQUEUE_WSOCK_HOST', 'localhost')
    WSOCK_PORT = getattr(settings, 'MQUEUE_WSOCK_PORT', 3000)
    WSOCK_ADMIN_HOST = getattr(settings, 'MQUEUE_WSOCK_ADMIN_HOST', 'localhost')
    WSOCK_ADMIN_PORT = getattr(settings, 'MQUEUE_WSOCK_ADMIN_PORT', 3001)

#LIVE_STREAM = True
register = template.Library()

@register.simple_tag
def get_channel_url(user):
    if LIVE_STREAM is True:
        if user.is_superuser:
            store = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
            # set a key for authentication on the websocket server
            key = generate_key()
            val = "admin"
            store.set(key, val)
            store.expire(key, 5)
            return 'http://'+WSOCK_ADMIN_HOST+':'+str(WSOCK_ADMIN_PORT)+'?k='+key
        else:
            return 'http://'+WSOCK_HOST+':'+str(WSOCK_PORT)
    return ''

@register.simple_tag
def public_channel_url():
    return 'http://'+WSOCK_HOST+':'+str(WSOCK_PORT)

@register.simple_tag
def admin_channel_url():
    return 'http://'+WSOCK_ADMIN_HOST+':'+str(WSOCK_ADMIN_PORT)
