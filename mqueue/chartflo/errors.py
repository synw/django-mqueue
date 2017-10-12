from altair import Data, Scale
from mqueue.models import MEvent
from chartflo.factory import ChartController

GENERATOR = "mqueue.errors"


def gen_errors(errors, warnings, slug,
               name="", time_unit="yearmonthdatehours",):
    chart = ChartController()
    x_options = {"labelAngle": -45.0}
    x = ("Date", "Date:T", x_options)
    y = ("Num", "sum(Num):Q")
    dataset = []
    for el in errors.order_by("date_posted"):
        data = {"Event class": "Error", "Num": 1,
                "Date": chart.serialize_date(el.date_posted)}
        dataset.append(data)
    for el in warnings.order_by("date_posted"):
        data = {"Event class": "Warning", "Num": 1,
                "Date": chart.serialize_date(el.date_posted)}
        dataset.append(data)
    q = Data(values=dataset)
    scale = Scale(bandSize=500)
    chart.generate(
        slug, name, "circle", q, x, y, 1200, 180,
        time_unit=time_unit, color="Event class:N",
        verbose=True, size="sum(Num):Q",
        generator=GENERATOR, modelnames="MEvent",
        scale=scale
    )


def run(e=None):
    global GENERATOR
    events = MEvent.objects.all()
    errors = events.filter(event_class__icontains="error")
    warnings = events.filter(event_class__icontains="warning")
    gen_errors(errors, warnings, "events_errors")
