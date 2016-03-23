# -*- coding: utf-8 -*-

from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from mqueue.models import MEvent, MonitoredModel, HighlyMonitoredModel, ObjectLevelMonitoredModel
from mqueue.conf import bcolors, MODELS_NOT_TO_MONITOR
from mqueue.utils import get_user, get_url, get_admin_url, get_object_name, get_subclasses


#~ utilities
def is_object_level_monitored(instance):
    parent_cls = instance.__class__.__bases__
    if ObjectLevelMonitoredModel in parent_cls:
        return True
    return False

def check_monitored_object(instance, created=True, deleted=False):
    create_event = True
    if is_object_level_monitored(instance):
        if instance.monitoring_level == 0:
            create_event = False
        if instance.monitoring_level == 1:
            if not created and not deleted:
                create_event = False
    return create_event

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
        create_event = check_monitored_object(instance, created)
        event_class = instance.__class__.__name__+' created'
        if create_event:
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
            
def mmessage_delete(sender, instance, **kwargs):
    #~ try to get the user
    user = get_user(instance)
    #~ try to get the object name
    obj_name = get_object_name(instance, user)
    #~ check for object level monitoring
    create_event = check_monitored_object(instance, deleted=True)
    event_class = instance.__class__.__name__+' deleted'
    if create_event:
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
    create_event = check_monitored_object(instance, created)
    if created:
        event_str = ' created'
    event_class = instance.__class__.__name__+event_str
    if create_event:
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


#~ register signals for monitored models
for subclass in get_subclasses(MonitoredModel):
    if subclass.__name__ not in MODELS_NOT_TO_MONITOR:
        post_save.connect(mmessage_create, subclass)
        post_delete.connect(mmessage_delete, subclass)
        
for subclass in get_subclasses(HighlyMonitoredModel):
    if subclass.__name__ not in MODELS_NOT_TO_MONITOR:
        post_save.connect(mmessage_save, subclass)
        post_delete.connect(mmessage_delete, subclass)
        
for subclass in get_subclasses(ObjectLevelMonitoredModel):
    if subclass.__name__ not in MODELS_NOT_TO_MONITOR:
        post_save.connect(mmessage_save, subclass)
        post_delete.connect(mmessage_delete, subclass)

    