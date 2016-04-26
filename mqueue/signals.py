# -*- coding: utf-8 -*-

from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from mqueue.models import MEvent
from mqueue.conf import bcolors, MODELS_NOT_TO_MONITOR
from mqueue.utils import get_user, get_url, get_admin_url, get_object_name


#~ signals
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
    if settings.DEBUG:
        print bcolors.SUCCESS+'Event'+bcolors.ENDC+' : object '+obj_name+event_str
    return


    