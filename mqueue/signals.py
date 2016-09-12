# -*- coding: utf-8 -*-

from django.conf import settings
from mqueue.models import MEvent
from mqueue.utils import get_user, get_url, get_admin_url, get_object_name
from mqueue.conf import bcolors
from mqueue.conf import LIVE_FEED
if LIVE_FEED is True:
    from mqueue_livefeed.conf import CHANNEL, EXTRA_CHANNELS, STREAM_MODELS, SITE_NAME
    from instant.producers import broadcast
    

def mmessage_create(sender, instance, created, **kwargs):
    if created:
        #~ try to get the user
        user = get_user(instance)
        #~ try to get the object name
        obj_name = get_object_name(instance, user)
        #~ try to get the admin url
        admin_url = get_admin_url(instance)
        #~ check for object level monitoring
        event_class = instance.__class__.__name__+' created'
        #~ create event
        MEvent.objects.create(
                    model = instance.__class__, 
                    name = obj_name, 
                    obj_pk = instance.pk, 
                    user = user,
                    url = get_url(instance),
                    admin_url = admin_url,
                    event_class = event_class,
                    )
        if LIVE_FEED is True and STREAM_MODELS is True:
            data = {"admin_url": admin_url, "site": SITE_NAME}
            broadcast(message=obj_name, event_class=event_class, channel=CHANNEL, data=data)
            if len(EXTRA_CHANNELS) > 0:
                for channel in EXTRA_CHANNELS:
                    broadcast(message=obj_name, event_class=event_class, channel=channel, data=data)
            
        if settings.DEBUG:
            print bcolors.SUCCESS+'Event'+bcolors.ENDC+' : object '+obj_name+' created'
    return
            
def mmessage_delete(sender, instance, **kwargs):
    #~ try to get the user
    user = get_user(instance)
    #~ try to get the object name
    obj_name = get_object_name(instance, user)
    #~ check for object level monitoring
    event_class = instance.__class__.__name__+' deleted'
    #~ create event
    MEvent.objects.create(
                model = instance.__class__, 
                name = obj_name, 
                obj_pk = instance.pk, 
                user = user,
                event_class = event_class,
                )
    if LIVE_FEED is True and STREAM_MODELS is True:
        data = {"site": SITE_NAME}
        broadcast(message=obj_name, event_class=event_class, channel=CHANNEL, data=data)
        if len(EXTRA_CHANNELS) > 0:
            for channel in EXTRA_CHANNELS:
                broadcast(message=obj_name, event_class=event_class, channel=channel, data=data)
    if settings.DEBUG:
        print bcolors.WARNING+'Event'+bcolors.ENDC+' : object '+obj_name+' deleted'
    return

def mmessage_save(sender, instance, created, **kwargs):
    #~ try to get the user
    user = get_user(instance)
    if 'name' not in kwargs.keys():
        #~ try to get the object name
        obj_name = get_object_name(instance, user)
    else:
        obj_name = kwargs('name')
    #~ try to get the admin url
    admin_url = get_admin_url(instance)
    event_str = ' edited'
    #~ check for object level monitoring
    if created:
        event_str = ' created'
    event_class = instance.__class__.__name__+event_str
    #~ create event
    MEvent.objects.create(
                model = instance.__class__, 
                name = obj_name, 
                obj_pk = instance.pk, 
                user = user,
                url = get_url(instance),
                admin_url = admin_url,
                event_class = event_class,
                )
    if LIVE_FEED is True and STREAM_MODELS is True:
        data = {"admin_url": admin_url, "site": SITE_NAME}
        broadcast(message=obj_name, event_class=event_class, channel=CHANNEL, data=data)
        if len(EXTRA_CHANNELS) > 0:
            for channel in EXTRA_CHANNELS:
                broadcast(message=obj_name, event_class=event_class, channel=channel, data=data)
    if settings.DEBUG:
        print bcolors.SUCCESS+'Event'+bcolors.ENDC+' : object '+obj_name+event_str
    return


    