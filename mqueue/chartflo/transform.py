from dataswim import ds


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


def relations():
    users = ds.load_("auth_user")
    ds.relation(users, "user_id", "username")
    ct = ds.load_("django_content_type")
    ds.relation(ct, "content_type_id", "model")
    ds.relation(ct, "content_type_id", "app_label")
    ds.to_csv("events.csv")


def errs_warnings():
    sp = ds.split_("type")
    err = sp["Error"]
    wa = sp["Warning"]
    ds2 = ds.concat_(err.df, wa.df)
    ds2.to_csv("errors_warnings.csv")


def run(**kwargs):
    """
    Transform data to get extra info columns
    """
    ds.load("mqueue_mevent")
    ds.date("date_posted")
    ds.dateindex("date_posted")
    ds.add("num", 1)
    ds.copy_col("event_class", "type")
    ds.apply(add_type, ["type"])
    relations()
    errs_warnings()
