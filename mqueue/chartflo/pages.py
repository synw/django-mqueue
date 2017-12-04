from altair import Scale
from django.conf import settings
from mqueue.models import MEvent


def run(events=None):
    from dataswim import ds
    q = MEvent.objects.all()
    data = q.filter(event_class__icontains="Page")
    ds.load_django(data)
    ds.date("date_posted")
    edits_all = ds.contains_("event_class", "edit")
    create_all = ds.contains_("event_class", "create")
    delete_all = ds.contains_("event_class", "delete")
    edits = edits_all.rsum_("1D", dateindex="date_posted")
    edits.add("operation_type", "edit")
    create = create_all.rsum_("1D", dateindex="date_posted")
    create.add("operation_type", "create")
    delete = delete_all.rsum_("1D", dateindex="date_posted")
    delete.add("operation_type", "delete")
    ds = ds.concat_(create.df, edits.df, delete.df)
    ds.engine = "altair"
    ds.opts(dict(color="operation_type:N", height=180, width=1040))
    x_opts = dict(labelAngle=0)
    x = ("Date", "date:T", x_opts)
    y = ("Number", "num:Q")
    scale = Scale(
        domain=['create', 'delete', 'edit'],
        range=['#e7ba52', '#c7c7c7', '#aec7e8'],
    ),
    ds.opts(dict(scale=scale))
    ds.chart(x, y, "bar")
    #c = ds.bar_(options=dict(barSize=10))
    ds.opts(dict(size="num:Q"))
    c = ds.point_()
    ds.stack("pages", c)
    ds.to_files()
