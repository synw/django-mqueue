# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.utils.html import format_html
from .models import MEvent
from .utils import format_event_class


def link_to_object(obj):
    return format_html('<a href="' + obj.url + '" target="_blank">' + obj.url + "</a>")


def link_to_object_admin(obj):
    return format_html(
        '<a href="' + obj.admin_url + '" target="_blank">' + obj.admin_url + "</a>"
    )


def event(obj):
    return format_html(format_event_class(obj))


@admin.register(MEvent)
class MEventAdmin(admin.ModelAdmin):
    date_hierarchy = "date_posted"
    readonly_fields = ["date_posted", "request"]
    list_display = [
        event,
        "name",
        "date_posted",
        "bucket",
        "user",
        link_to_object,
        link_to_object_admin,
        "scope",
    ]
    list_filter = (
        "event_class",
        ("content_type", admin.RelatedOnlyFieldListFilter),
        ("user", admin.RelatedOnlyFieldListFilter),
        "scope",
    )
    search_fields = ["name", "user__username", "event_class", "bucket"]
    link_to_object.allow_tags = True
    link_to_object.short_description = _(u"See on site")
    link_to_object_admin.allow_tags = True
    link_to_object_admin.short_description = _(u"See in admin")
    format_event_class.allow_tags = True
    format_event_class.short_description = _(u"Class")
    filters_on_top = True
    list_select_related = (
        "user",
        "content_type",
    )

    class Media:
        css = {
            "all": (
                "mqueue/mqueue.css",
                "https://cdn.jsdelivr.net/npm/font-awesome@4.7.0"
                + "/css/font-awesome.min.css",
            )
        }

    def get_readonly_fields(self, request, obj=None):
        super(MEventAdmin, self).get_readonly_fields(request, obj)
        return ("notes", "request")
