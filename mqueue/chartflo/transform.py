from dataswim import ds
from django.conf import settings
from django.utils._os import safe_join
from mqueue.models import MEvent


datapath = safe_join(settings.BASE_DIR, "data")


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
    elif "deleted" in val:
        return "Delete"
    else:
        return "Other"


def run(events=None):
    """
    Transform data to get extra info columns
    """
    global datapath
    events = MEvent.objects.all()
    ds.load_django(events)
    ds.date("date_posted")
    ds.dateindex("date_posted")
    ds.add("num", 1)
    ds.copy_col("event_class", "type")
    ds.apply(add_type, ["type"])
    ds.to_csv(datapath + "/events.csv")
