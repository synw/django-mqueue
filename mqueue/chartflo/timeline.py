from dataswim import ds
from django.conf import settings


def run(events=None):
    ds.connect('postgresql://djangouser:Xh327eMV@localhost/econso30')
    ds.load("mqueue_mevent")
    ds.date("date_posted")
    ds.dateindex("date_posted")
    ds.add("num", 1)
    ds.copy_col("event_class", "type")

    def add_type(val):
        val = val[0]
        if "ERROR" in val:
            return "Error"
        elif "WARNING" in val:
            return "Warning"
        elif "created" in val:
            return "Create"
        elif "edited" in val:
            return "Edit"
        else:
            return "Other"

    ds.apply(add_type, ["type"])
    ds.engine = "altair"
    x_opts = dict(labelAngle=360, size="sum(num):Q")
    x = ("date_posted", "date_posted:T", x_opts)
    y = ("num", "sum(num):Q")
    ds.opts(dict(color="event_class:N", time_unit="yearmonthdate",
                 height=250, width=1040, shape="type:N"))
    #chart.draw(events, x, y, "line", num_col=("num", 1), index_col="date_posted", opts=opts)
    # ds.show()
    ds.chart(x, y)
    c = ds.point_()
    ds.stack("events_timeline", "Timeline", c)
    path = settings.BASE_DIR + "/templates/dashboards/mqueue/charts"
    ds.to_files(path)
