from chartflo.widgets import sparkline
from .transform import last_weeks


def run(events=None):
    errs, edits = last_weeks()
    sparkline.simple("errors", errs, "mqueue")
    sparkline.simple("edits", edits, "mqueue")
