from __future__ import print_function
from mqueue.models import MEvent
from chartflo.charts import chart, number


def gen_errors(errors, warnings):
    x_options = {"labelAngle": -45.0}
    x = ("Date", "Date:T", x_options)
    y = ("Num", "sum(Num):Q")
    chart.engine = "altair"
    opts = {}
    opts["size"] = "sum(Num):Q"
    opts["time_unit"] = "yearmonthdatehours"
    opts["width"] = 1040
    opts["height"] = 250
    opts["color"] = "Event class"
    dataset = []
    for el in errors.order_by("date_posted"):
        data = {"Event class": "Error", "Num": 1,
                "Date": chart.serialize_date(el.date_posted)}
        dataset.append(data)
    for el in warnings.order_by("date_posted"):
        data = {"Event class": "Warning", "Num": 1,
                "Date": chart.serialize_date(el.date_posted)}
        dataset.append(data)
    c = chart.draw(dataset, x, y, "circle", opts=opts)
    chart.stack("errors_warnings", "Errors and warnings", c)


def gen_nums(events):
    val = events.count()
    number.generate("events", "Events", val, verbose=True,
                    generator="mqueue", modelnames="MEvent", dashboard="mqueue",
                    icon="flash")
    errs = events.filter(event_class__icontains='ERROR').count()
    number.generate("errors", "Errors", errs, verbose=True,
                    generator="mqueue", modelnames="MEvent", dashboard="mqueue",
                    icon="bug", color="red")
    wa = events.filter(event_class__icontains='WARNING').count()
    number.generate("warnings", "Warnings", wa, verbose=True,
                    generator="mqueue", modelnames="MEvent", dashboard="mqueue",
                    icon="warning", color="orange")
    logins = events.filter(event_class__icontains='login').count()
    number.generate("logins", "Logins", logins, verbose=True,
                    generator="mqueue", modelnames="MEvent", dashboard="mqueue",
                    icon="user", color="blue")
    edits = events.filter(event_class__icontains='edit').count()
    number.generate("edits", "Edits", edits, verbose=True,
                    generator="mqueue", modelnames="MEvent", dashboard="mqueue",
                    icon="save", color="blue")


def run(e=None):
    print("Generating charts for events")
    events = MEvent.objects.all()
    errors = events.filter(event_class__icontains="error")
    warnings = events.filter(event_class__icontains="warning")
    gen_errors(errors, warnings)
    gen_nums(events)
    chart.export("dashboards/mqueue/charts")
