from django.conf import settings
from django.utils._os import safe_join
from dataswim import ds
from .transform import run as transform
from .errors import run as errors
from .timeline import run as timeline
from .event_class import run as ec
from .sparklines import run as sp


def run(events=None):
    ds.datapath = safe_join(settings.BASE_DIR, "data")
    transform()
    path = safe_join(settings.BASE_DIR, "data")
    ds.load_csv(path + "/events.csv")
    ds.date("date_posted")
    ds.backup()
    errors()
    ds.restore()
    timeline()
    ec()
    sp()
    path = settings.BASE_DIR + "/templates/dashboards/mqueue/charts"
    ds.to_files(path)
