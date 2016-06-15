# -*- coding: utf-8 -*-

from collections import OrderedDict
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response
from django.contrib import admin
from admin_views.admin import AdminViews
from mqueue.models import MEvent
from mqueue.conf import EVENT_CLASSES, EVENT_ICONS_HTML, EVENT_EXTRA_HTML


def link_to_object(obj):
    return '<a href="'+obj.url+'" target="_blank">'+obj.url+'</a>'

def link_to_object_admin(obj):
    return '<a href="'+obj.admin_url+'" target="_blank">'+obj.admin_url+'</a>'

def get_event_class_str(obj):
    event_class_str = 'Default'
    if 'created' in obj.event_class:
        event_class_str = 'Object created'
    if 'deleted' in obj.event_class:
        event_class_str = 'Object deleted'
    if 'edited' in obj.event_class:
        event_class_str = 'Object edited'
    return event_class_str

def format_event_class(obj):
    event_html = ''
    printed_class = get_event_class_str(obj)
    icon = ''
    if obj.event_class in EVENT_ICONS_HTML.keys():
        icon = EVENT_ICONS_HTML[obj.event_class]+'&nbsp;'
        printed_class = obj.event_class
    else:
        if 'created' in obj.event_class:
            icon = EVENT_ICONS_HTML['Object created']+'&nbsp;'
        elif 'edited' in obj.event_class:
            icon = EVENT_ICONS_HTML['Object edited']+'&nbsp;'
        elif 'deleted' in obj.event_class:
            icon = EVENT_ICONS_HTML['Object deleted']+'&nbsp;'
        else:
            icon = EVENT_ICONS_HTML['Default']+'&nbsp;'
        if 'error' in obj.event_class.lower():
            icon = EVENT_ICONS_HTML['Error']+'&nbsp;'
            printed_class = 'Error'
        elif 'debug' in obj.event_class.lower():
            icon = EVENT_ICONS_HTML['Debug']+'&nbsp;'
            printed_class = 'Debug'
        elif 'warning' in obj.event_class.lower():
            icon = EVENT_ICONS_HTML['Warning']+'&nbsp;'
            printed_class = 'Warning'
        elif 'info' in obj.event_class.lower():
            icon = EVENT_ICONS_HTML['Info']+'&nbsp;'
            printed_class = 'Info'
        elif 'important' in obj.event_class.lower():
            icon = EVENT_ICONS_HTML['Important']+'&nbsp;'
            printed_class = 'Important'
        #event_class_str = obj.event_class.replace('Object', model.__name__)
    if obj.event_class in EVENT_CLASSES.keys():
        event_html += '<span class="'+EVENT_CLASSES[printed_class]+'">'+icon+obj.event_class+'</span>'
    else:
        event_html += '<span class="'+EVENT_CLASSES[printed_class]+'">'+icon+obj.event_class+'</span>'
    if obj.event_class in EVENT_EXTRA_HTML.keys():
        event_html += EVENT_EXTRA_HTML[obj.event_class]
    return event_html
    
    
@admin.register(MEvent)
class MEventAdmin(AdminViews):
    date_hierarchy = 'date_posted'
    readonly_fields = ['date_posted', 'request']
    list_display = ['name', link_to_object, link_to_object_admin, 'content_type', 'user', 'date_posted', format_event_class]
    list_filter = (
        'event_class',
        ('content_type', admin.RelatedOnlyFieldListFilter),
        ('user', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ['name', 'user__username', 'event_class']
    link_to_object.allow_tags = True   
    link_to_object.short_description = _(u'See on site')
    link_to_object_admin.allow_tags = True   
    link_to_object_admin.short_description = _(u'See in admin')
    format_event_class.allow_tags = True   
    format_event_class.short_description = _(u'Class')
    filters_on_top = True
    
    list_select_related = (
        'user',
        'content_type',
    )
    
    def get_readonly_fields(self, request, obj=None):
        super(MEventAdmin, self).get_readonly_fields(request, obj)
        if 'log' in obj.event_class.lower():
            return ('notes', 'request')
        else:
            return ('request',)
        
    admin_views =   (
                    ('Stats', 'stats'),
                    )

    def stats(self, *args, **kwargs):
        allevents = MEvent.objects.all().prefetch_related()
        # count events for class
        events_by_class = {}
        for event in allevents.order_by('event_class'):
            if event.event_class in events_by_class.keys():
                events_by_class[event.event_class] = events_by_class[event.event_class]+1
            else:
                events_by_class[event.event_class] = 1
        # count events for user
        events_by_user = {}
        for event in allevents.order_by('user'):
            if event.user:
                if event.user.username in events_by_user.keys():
                    events_by_user[event.user.username] = events_by_user[event.user.username]+1
                else:
                    events_by_user[event.user.username] = 1
            else:
                if _(u'No user') in events_by_user.keys():
                    events_by_user[_(u'No user')] = events_by_user[_(u'No user')]+1
                else:
                    events_by_user[_(u'No user')] = 1
        # count events for models
        events_by_model = {}
        for event in allevents.order_by('content_type'):
            if event.content_type:
                ct = str(event.content_type).title()
                if ct in events_by_model.keys():
                    events_by_model[ct] = events_by_model[ct]+1
                else:
                    events_by_model[ct] = 1
            else:
                if _(u'No model') in events_by_model.keys():
                    events_by_model[_(u'No model')] = events_by_model[_(u'No model')]+1
                else:
                    events_by_model[_(u'No model')] = 1
        # events overtime
        events_overtime = OrderedDict()
        for event in allevents.order_by('date_posted'):
            event_date = event.date_posted.strftime("%Y-%m-%d")
            if event_date in events_overtime.keys():
                events_overtime[event_date] = events_overtime[event_date]+1
            else:
                events_overtime[event_date] = 1
        datapack_overtime = {'chart_id': 'chart_overtime','data_label': 'events', 'dataset': events_overtime}
        datapack_models = {'chart_id': 'chart_by_model','data_label': 'events','dataset': events_by_model,'legend': False,}
        datapack_users = {'chart_id': 'chart_by_user','data_label': 'events','dataset': events_by_user,'legend': False,}
        datapack_classes = {'chart_id': 'chart_by_classes','data_label': 'events','dataset': events_by_class,'legend': False,}
        return render_to_response('admin/mqueue/stats.html',
                                    {
                                     'datapack_classes': datapack_classes,
                                     'datapack_users': datapack_users,
                                     'datapack_models': datapack_models,
                                     'datapack_overtime': datapack_overtime,
                                     },
                                    )

        

    


