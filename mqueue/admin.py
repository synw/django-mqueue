# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mqueue.models import MEvent
from mqueue.conf import EVENT_CLASSES, EVENT_EXTRA_HTML, EVENT_ICONS_HTML


EVENT_CLASSES=getattr(settings, 'MQUEUE_EVENT_CLASSES', EVENT_CLASSES)
EVENT_EXTRA_HTML=getattr(settings, 'EVENT_EXTRA_HTML', EVENT_EXTRA_HTML)
EVENT_ICONS_HTML=getattr(settings, 'EVENT_ICONS_HTML', EVENT_ICONS_HTML)


def link_to_object(obj):
    return '<a href="'+obj.url+'" target="_blank">'+obj.url+'</a>'

def link_to_object_admin(obj):
    return '<a href="'+obj.admin_url+'" target="_blank">'+obj.admin_url+'</a>'

def format_event_class(obj):
    event_html = ''
    icon = ''
    if obj.event_class in EVENT_ICONS_HTML.keys():
        icon = EVENT_ICONS_HTML[obj.event_class]+'&nbsp;'
    else:
        icon = EVENT_ICONS_HTML['Default']+'&nbsp;'
    if obj.event_class in EVENT_CLASSES.keys():
        event_html += '<span class="'+EVENT_CLASSES[obj.event_class]+'">'+icon+obj.event_class+'</span>'
    else:
        event_html += '<span class="'+EVENT_CLASSES['Default']+'">'+icon+obj.event_class+'</span>'
    if obj.event_class in EVENT_EXTRA_HTML.keys():
        event_html += EVENT_EXTRA_HTML[obj.event_class]
    return event_html
    
def format_content_type(obj):
    if obj.content_type:
        return obj.content_type.name
    else:
        return ''

def format_user(obj):
    if obj.user:
        return obj.user.username
    else:
        return ''
    
    
@admin.register(MEvent)
class MEventAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_posted'
    read_only = ['date_posted']
    list_display = ['name', link_to_object, link_to_object_admin, format_content_type, 'date_posted', format_user, format_event_class]
    list_filter = (
        'event_class',
        'content_type',
        ('user', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'user__username', 'event_class']
    link_to_object.allow_tags = True   
    link_to_object.short_description = _(u'See on site')
    link_to_object_admin.allow_tags = True   
    link_to_object_admin.short_description = _(u'See in admin')
    format_event_class.allow_tags = True   
    format_event_class.short_description = _(u'Class')
    format_user.short_description = _(u'User')
    format_content_type.short_description = _(u'Content type')
    

    
    


