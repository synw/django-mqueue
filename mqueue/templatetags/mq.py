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

#LIVE_STREAM = True
register = template.Library()

@register.simple_tag
def get_channel_url(user):
    if LIVE_STREAM is True:
        stream_class = 'public'
        if user.is_authenticated():
            stream_class = 'logged_in_user'
        if user.is_staff:
            stream_class = 'staff'
        if user.is_superuser:
            stream_class = 'admin'
        print stream_class
        store = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        if stream_class == 'public':
            key = 'p'
        else:
            # set a key for authentication on the websocket server
            key = generate_key()
            store.set(key, stream_class)
            store.expire(key, 3)
        return 'http://'+WSOCK_HOST+':'+str(WSOCK_PORT)+'?k='+key
    return ''

@register.simple_tag
def channel_url():
    return 'http://'+WSOCK_HOST+':'+str(WSOCK_PORT)
