# -*- coding: utf-8 -*-
from dataswim import ds


def edits_del_create():
    global ds
    ds = ds.vals_("type")
    ds.engine = "bokeh"
    ds.drop_rows("Warning", "Error", "Other")
    ds.width(300)
    ds.height(250)
    ds.rename("type", "Type")
    ds.chart("Type", "Number")
    c = ds.bar_()
    ds.stack("edit_del_create", c)


def event_class():
    global ds
    ds = ds.vals_("event_class", "Event class", "Number of events")
    ds.engine = "altair"
    x = ("Number of events", "sum(Number of events):Q")
    y = ("Event class", "Event class:N")
    ds.width(400)
    ds.opts(dict(color="Event class:N"))
    ds.chart(x, y)
    c = ds.bar_()
    ds.stack("event_classes", c)


def timeline():
    ds.engine = "altair"
    x_opts = dict(labelAngle=360, size="sum(num):Q")
    x = ("date_posted", "date_posted:T", x_opts)
    y = ("Number", "sum(num):Q")
    ds.width(940)
    ds.rename("event_class", "Event class")
    ds.rename("type", "Type")
    ds.opts(dict(color="Event class:N", time_unit="yearmonthdate",
                 height=250, shape="Type:N"))
    ds.chart(x, y)
    c = ds.point_()
    ds.stack("events_timeline", c)


def run(**kwargs):
    ds.reports = []
    ds.load_csv(ds.datapath+"/events.csv")
    ds.backup()
    timeline()
    ds.restore()
    event_class()
    ds.restore()
    edits_del_create()
    ds.restore()
    ds.to_files(ds.report_path+"/charts")
