# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mqueue.models import MEvent


def link_to_object(obj):
    return '<a href="'+obj.url+'" target="_blank">'+obj.url+'</a>'


@admin.register(MEvent)
class MEventAdmin(admin.ModelAdmin):
    read_only = ['date_posted', 'content_type']
    list_display = ['name', link_to_object, 'content_type', 'date_posted']
    link_to_object.allow_tags = True   
    link_to_object.short_description = _(u'See')


