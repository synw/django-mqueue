# -*- coding: utf-8 -*-

from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from mqueue.models import MEvent, MonitoredModel
from mqueue.conf import bcolors


MODELS_NOT_TO_MONITOR = getattr(settings, 'MQUEUE_STOP_MONITORING', None)


def get_subclasses(cls):
    result = [cls]
    classes_to_inspect = [cls]
    while classes_to_inspect:
        class_to_inspect = classes_to_inspect.pop()
        for subclass in class_to_inspect.__subclasses__():
            if subclass not in result:
                result.append(subclass)
                classes_to_inspect.append(subclass)
    return result

def get_object_name(instance):
    obj_name = 'Object'
    try:
        obj_name = instance.name
    except:
        try:
            obj_name = instance.title
        except:
            try:
                obj_name = instance.slug 
            except:
                pass
    return obj_name

def get_user(instance):
    user = None
    try:
        user = instance.user
        print 'user='+str(instance.user)
    except:
        try:
            user = instance.editor
        except:
            pass
    return user

def get_admin_url(instance, _kwargs):
    admin_url = ''
    obj_pk = ''
    try:
        obj_pk = instance.pk
    except:
        pass
    if obj_pk:
        admin_url = reverse('admin:%s_%s_change' %(instance._meta.app_label,  instance._meta.model_name),  args=[instance.id] )
    return admin_url
    
def mmessage_save(sender, instance, created, **kwargs):
    if created:
        #~ try to get the object name
        obj_name = get_object_name(instance)
        #~ try to get the user
        current_user = get_user(instance)
        #~ try to get the admin url
        admin_url = get_admin_url(instance, kwargs)
        #~ create event
        MEvent.events.create(
                    model = instance.__class__, 
                    name = obj_name, 
                    obj_pk = instance.pk, 
                    user = current_user,
                    admin_url = admin_url,
                    event_class = 'Object created'
                    )
        if settings.DEBUG:
            print bcolors.SUCCESS+'Event'+bcolors.ENDC+' : object '+obj_name+' created'
            
def mmessage_delete(sender, instance, **kwargs):
    #~ try to get the object name
    obj_name = get_object_name(instance)
    #~ try to get the user
    user = get_user(instance)
    #~ create event
    MEvent.events.create(
                model = instance.__class__, 
                name = obj_name, 
                obj_pk = instance.pk, 
                user = user,
                event_class = 'Object deleted'
                )
    if settings.DEBUG:
        print bcolors.WARNING+'Event'+bcolors.ENDC+' : object '+obj_name+' deleted'

#~ register signals for monitored models
for subclass in get_subclasses(MonitoredModel):
    if subclass.__name__ not in MODELS_NOT_TO_MONITOR:
        post_save.connect(mmessage_save, subclass)
        post_delete.connect(mmessage_delete, subclass)


    