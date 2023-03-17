import json
from django.forms.models import model_to_dict
from django.contrib.auth.models import Group
from mqueue.models import MEvent

MEvent.objects.create(name = 'A group event', model=Group)
MEvent.objects.create(name = 'A group event', model=Group)

for event in list(
  MEvent.objects.events_for_model(Group)
):
  print(f"- {event}")