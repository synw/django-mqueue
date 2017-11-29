from __future__ import print_function
from dataswim import ds
from mqueue.models import MEvent
from chartflo.serializers import convert_dataset
from chartflo.widgets import number


def gen_errors(errors, warnings):
    x_options = {"labelAngle": -45.0}
    x = ("Date", "Date:T", x_options)
    y = ("Num", "sum(Num):Q")
    ds.engine = "altair"
    opts = {}
    #opts["size"] = "sum(Num):Q"
    opts["time_unit"] = "yearmonthdatehours"
    opts["width"] = 1040
    opts["height"] = 250
    opts["color"] = "Event class"
    dataset = []
    # ds.date("date_posted")
    for el in errors.order_by("date_posted"):
        data = {"Event class": "Error", "Num": 1,
                "Date": ds.format_date_(el.date_posted)}
        dataset.append(data)
    for el in warnings.order_by("date_posted"):
        data = {"Event class": "Warning", "Num": 1,
                "Date": ds.format_date_(el.date_posted)}
        dataset.append(data)
    ds.df = convert_dataset(dataset, "Event class", "Date")
    ds.opts(opts)
    c = ds.chart_(x, y, "point")
    ds.stack("errors_warnings", "Errors and warnings", c)


def gen_small():
    ds.load_csv(ds.datapath + "/events.csv")
    ds = ds.contains_("event_class", "Log")
    x_opts = dict(labelAngle=360)
    x = ("Date", "date_posted:T", x_opts)
    y = ("Events", "sum(num):Q")
    ds.opts(dict(color="event_class:N",
                 time_unit="yearmonthdate", height=200, width=640))
    ds.chart(x, y)
    c = ds.point_()
    ds.stack("errors_small", "Errors and warnings", c)


def gen_nums(events):
    val = events.count()
    number.simple("events", val, "Events", dashboard="mqueue", icon="flash")
    errs = events.filter(event_class__icontains='ERROR').count()
    number.simple("errors", errs, "Error", dashboard="mqueue",
                  icon="bug", color="red")
    wa = events.filter(event_class__icontains='WARNING').count()
    number.simple("warnings", wa, "Warnings", dashboard="mqueue",
                  icon="warning", color="orange")
    logins = events.filter(event_class__icontains='login').count()
    number.simple("logins", logins, "Logins",
                  dashboard="mqueue", icon="user", color="blue")
    edits = events.filter(event_class__icontains='edit').count()
    number.simple("edits", edits, "Edits",
                  dashboard="mqueue", icon="save", color="blue")
    e404 = events.filter(name__icontains='Not found').count()
    number.simple("err404", e404, "404",
                  dashboard="mqueue", icon="random", color="blue")
    e500 = events.filter(name__icontains='Internal server error').count()
    number.simple("err500", e500, "500",
                  dashboard="mqueue", icon="ambulance", color="blue")


def run(e=None):
    print("Generating charts for events")
    events = MEvent.objects.all()
    errors = events.filter(event_class__icontains="error")
    warnings = events.filter(event_class__icontains="warning")
    gen_nums(events)
    # gen_errs()
    gen_errors(errors, warnings)
    # gen_small()
