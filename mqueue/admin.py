# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mqueue.models import MEvent
from mqueue.conf import EVENT_CLASSES


EVENT_CLASSES=getattr(settings, 'MQUEUE_EVENT_CLASSES', EVENT_CLASSES)


def link_to_object(obj):
    return '<a href="'+obj.url+'" target="_blank">'+obj.url+'</a>'

def link_to_object_admin(obj):
    return '<a href="'+obj.admin_url+'" target="_blank">'+obj.admin_url+'</a>'

def format_event_class(obj):
    if obj.event_class in EVENT_CLASSES.keys():
        return '<span class="'+EVENT_CLASSES[obj.event_class]+'">'+obj.event_class+'</span>'
    else:
        return '<span class="'+EVENT_CLASSES['Default']+'">'+obj.event_class+'</span>'


@admin.register(MEvent)
class MEventAdmin(admin.ModelAdmin):
    read_only = ['date_posted', 'event_class', 'content_type']
    list_display = ['name', link_to_object, link_to_object_admin, 'content_type', 'date_posted', 'user', format_event_class]
    search_fields = ['name', 'user__username']
    link_to_object.allow_tags = True   
    link_to_object.short_description = _(u'See on site')
    link_to_object_admin.allow_tags = True   
    link_to_object_admin.short_description = _(u'See in admin')
    format_event_class.allow_tags = True   
    format_event_class.short_description = _(u'Class')
    

    
    


