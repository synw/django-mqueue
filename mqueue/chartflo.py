# -*- coding: utf-8 -*-

from __future__ import print_function
from datetime import timedelta
from altair import Data
from mqueue.models import MEvent
from chartflo.factory import ChartController, NumberController
from django.utils import timezone


GENERATOR = "mqueue"


def encode(events, errors, warnings):
    dataset = []
    chart = ChartController()
    for event in errors.order_by("event_class"):
        data = {"class": "errors", "event_class": event.event_class,
                "date": chart.serialize_date(event.date_posted)}
        dataset.append(data)
    for event in warnings.order_by("event_class"):
        data = {"class": "warnings", "event_class": event.event_class,
                "date": chart.serialize_date(event.date_posted)}
        dataset.append(data)
    for event in events.order_by("event_class"):
        data = {"class": "events", "event_class": event.event_class,
                "date": chart.serialize_date(event.date_posted)}
        dataset.append(data)
    return dataset


def gen_multiline(events, errors, warnings, slug="events_multi", name=""):
    global GENERATOR
    dataset = encode(events, errors, warnings)
    chart = ChartController()
    x_options = {"labelAngle": -45.0, "axisWidth": 20.0}
    x = ("date", "date:T", x_options)
    y = ("event_class", "count(event_class):Q")
    q = Data(values=dataset)
    chart.generate_series(
        slug, name, "circle", q, x, y, 870, 180,
        time_unit="yearmonthdatehoursminutes", color="event_class:N",
        size="count(event_class):Q", verbose=True,
        generator=GENERATOR, modelnames="MEvent"
    )


def run(events):
    """
    Run the job
    """
    global GENERATOR
    events = MEvent.objects.all()
    num = NumberController()
    # Num users
    val = events.count()
    num.generate("events", "Events", val, verbose=True,
                 generator=GENERATOR, modelnames="MEvent")
    errors = events.filter(event_class__icontains="error")
    val = errors.count()
    num.generate("errors", "Errors", val, verbose=True,
                 generator=GENERATOR, modelnames="MEvent")
    warnings = events.filter(event_class__icontains="warning")
    val = warnings.count()
    num.generate("warnings", "Warnings", val, verbose=True,
                 generator=GENERATOR, modelnames="MEvent")
    val = events.filter(event_class__icontains="created").count()
    num.generate("created", "Objects created", val, verbose=True,
                 generator=GENERATOR, modelnames="MEvent")
    val = events.filter(event_class__icontains="updated").count()
    num.generate("updated", "Objects updated", val, verbose=True,
                 generator=GENERATOR, modelnames="MEvent")
    val = events.filter(event_class__icontains="deleted").count()
    num.generate("deleted", "Objects deleted", val, verbose=True,
                 generator=GENERATOR, modelnames="MEvent")
    # Last logins chart
    chart = ChartController()
    x_options = {"labelAngle": 0.0, "axisWidth": 10.0}
    x = ("date_posted", "date_posted:T", x_options)
    y = ("name", "count(name):Q")
    q = events
    chart.generate_series(
        "events_timeline", "", "line", q, x, y, 870, 180,
        time_unit="yearmonthdate", verbose=True,
        generator=GENERATOR, modelnames="MEvent"
    )
    # event class
    x_options = {"labelAngle": -45.0, "axisWidth": 10.0}
    x = ("event_class", "event_class:N", x_options)
    y = ("name", "name:Q")
    dataset = {}
    for event in events:
        if event.event_class not in dataset:
            dataset[event.event_class] = 1
        else:
            dataset[event.event_class] += 1
    chart.generate(
        "event_classes", "Event classes", "bar", dataset, x, y, 800, 250,
        color="event_class", verbose=True,
        generator=GENERATOR, modelnames="MEvent"
    )
    # generate all events chart
    gen_multiline(events, errors, warnings)
    date = timezone.now() - timedelta(days=1)
    events = events.filter(date_posted__gte=date)
    errors = errors.filter(date_posted__gte=date)
    warnings = warnings.filter(date_posted__gte=date)
    gen_multiline(events, errors, warnings,
                  slug="events_last_day", name="Last 24h events")
