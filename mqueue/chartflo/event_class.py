from dataswim import ds


def run(events=None):
    ds.restore()
    ds.dateindex("date_posted")
    ds.add("num", 1)
    ds.vals("event_class")
    ds.rename("event_class", "Number of events")
    ds.index_col("Event class")
    ds.engine = "altair"
    x = ("Number of events", "sum(Number of events):Q")
    y = ("Event class", "Event class:N")
    ds.opts(dict(color="Event class:N", height=400))
    ds.chart(x, y)
    c = ds.bar_()
    ds.stack("event_classes", c, "Events classes")
    #path = settings.BASE_DIR + "/templates/dashboards/mqueue/charts"
    # ds.to_files(path)
