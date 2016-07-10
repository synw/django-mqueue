# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.http import HttpResponseForbidden
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mqueue.models import MEvent
from mqueue.utils import format_event_class


def link_to_object(obj):
    return '<a href="'+obj.url+'" target="_blank">'+obj.url+'</a>'

def link_to_object_admin(obj):
    return '<a href="'+obj.admin_url+'" target="_blank">'+obj.admin_url+'</a>'
    
    
@admin.register(MEvent)
class MEventAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_posted'
    readonly_fields = ['date_posted', 'request']
    list_display = [format_event_class, 'name', 'date_posted', 'content_type', 'user', link_to_object, link_to_object_admin]
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

    


