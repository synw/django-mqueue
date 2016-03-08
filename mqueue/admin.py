# -*- coding: utf-8 -*-

from django.contrib import admin
from mqueue.models import ModerationEvent


def link_to_object(obj):
    return '<a href="'+obj.url+'" target="_blank">'+obj.url+'</a>'


@admin.register(ModerationEvent)
class ModeratedObjectAdmin(admin.ModelAdmin):
    read_only = ['date_posted', 'content_type']
    list_display = ['name', link_to_object, 'content_type', 'date_posted']
    link_to_object.allow_tags = True   
    link_to_object.short_description = 'Voir sur le site'


