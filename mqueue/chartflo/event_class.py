from dataswim import ds
from django.conf import settings
from mqueue.models import MEvent


def run(events=None):
    q = MEvent.objects.all()
    ds.load_django(q)
    ds.date("date_posted")
    ds.dateindex("date_posted")
    ds.add("num", 1)
    ds.vals("event_class")
    ds.rename("event_class", "Number of events")
    ds.index_col("Event class")
    ds.engine = "altair"
    x = ("Number of events", "Number of events:Q")
    y = ("Event class", "Event class:N")
    ds.opts(dict(color="Event class:N"))
    ds.chart(x, y)
    c = ds.bar_()
    ds.stack("event_classes", "Events classes", c)
    path = settings.BASE_DIR + "/templates/dashboards/mqueue/charts"
    ds.to_files(path)
