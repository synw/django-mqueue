from dataswim import ds


def run(events=None):
    ds.restore()
    ds.engine = "altair"
    x_opts = dict(labelAngle=360)
    x = ("date_posted", "date_posted:T", x_opts)
    y = ("num", "sum(num):Q")
    ds.opts(dict(color="event_class:N", time_unit="yearmonthdate",
                 height=250, width=1040, shape="type:N", size="sum(num):Q"))
    ds.chart(x, y)
    c = ds.point_()
    ds.stack("events_timeline", "Timeline", c)
