from dataswim import ds
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from mqueue.models import MEvent


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


def last_weeks():
    """
    Returns datapoints for the last 5 weeks
    """
    ds.load_csv(ds.datapath + "/events_typed.csv")
    ds.sort("date_posted")
    ds.dateindex("date_posted")
    ds.add("num", 1)
    w = ds.range_(weeks=10)
    s = w.split_("type")
    errs = ds.concat_(s["Error"].df, s["Warning"].df)
    errs.backup()
    edits = ds.concat_(s["Edit"].df, s["Create"].df)
    errs.rsum("1W")
    errs.fill_nan(0, "num")
    errs.to_int("num")
    errs_s = list(errs.df["num"])
    edits.rsum("1W")
    edits.fill_nan(0, "num")
    edits.to_int("num")
    edits_s = list(edits.df["num"])
    pages = w.contains_("event_class", "Page")
    pages.rsum("1W")
    pages.fill_nan(0, "num")
    pages.to_int("num")
    pages_s = list(errs.df["num"])
    return errs_s, edits_s, pages_s


def relations():
    q = User.objects.all()
    users = ds.load_django_(q)
    ds.relation(users, "user_id", "username")
    q = ContentType.objects.all()
    ct = ds.load_django_(q)
    ds.relation(ct, "content_type_id", "model")
    ds.relation(ct, "content_type_id", "app_label")
    ds.to_csv(ds.datapath + "/events.csv")


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
    ds.to_csv(ds.datapath + "/events_typed.csv")
    relations()
