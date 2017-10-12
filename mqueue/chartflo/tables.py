# -*- coding: utf-8 -*-

from __future__ import print_function
from tabular.models import Table
from tabular.factory import table
from chartflo.factory import OK
from mqueue.models import MEvent


def run(events=None):
    if events is None:
        q = MEvent.objects.all().order_by("-date_posted")
    else:
        q = events.order_by("-date_posted")
    instance, _ = Table.objects.get_or_create(slug="all_events")
    instance.name = "All events"
    instance.generator = "mqueue"
    instance.modelnames = "MEvent"
    fields = ["date_posted", "event_class", "name", "url"]
    instance.html = table.generate("all_events", q, fields)
    instance.save()
    instance.generate()
    print(OK + "Generated instance for all events")
