# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from mqueue.utils import generate_key
from mqueue.conf import GLOBAL_STREAMS, LIVE_STREAM, REDIS_HOST, REDIS_PORT, REDIS_DB, WSOCK_HOST, WSOCK_PORT, SITE_NAME, SITE_SLUG
if LIVE_STREAM is True:
    import redis


register = template.Library()

@register.simple_tag
def get_channel_url(user):
    if LIVE_STREAM is True:
        user_class = 'anonymous'
        if user.is_authenticated():
            user_class = 'user'
        if user.is_staff:
            user_class = 'staff'
        if user.is_superuser:
            user_class = 'admin'
        store = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
        if user_class == 'anonymous':
            key = 'p'
        else:
            # set a key for authentication on the websocket server
            key = generate_key()
            if user_class == 'anonymous':
                username = user_class
            else:
                username = user.username
            # pack related info and send it to redis
            site_slug = SITE_SLUG
            site_name = SITE_NAME
            if user_class in GLOBAL_STREAMS:
                site_slug = ''
                site_name = ''
            vals = {'user_class': user_class, 'username':username, 'site_slug':site_slug, 'site_name':site_name}
            store.hmset(key, vals)
            store.expire(key, 3)
        return 'http://'+WSOCK_HOST+':'+str(WSOCK_PORT)+'?k='+key
    return ''

@register.simple_tag
def channel_url():
    return 'http://'+WSOCK_HOST+':'+str(WSOCK_PORT)
