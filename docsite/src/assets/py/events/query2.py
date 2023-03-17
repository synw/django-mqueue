import json
from django.forms.models import model_to_dict
from django.contrib.auth.models import Group, User
from mqueue.models import MEvent

g1, _ = Group.objects.get_or_create(name="g1")
g2, _ = Group.objects.get_or_create(name="g2")

MEvent.objects.create(name = 'A group event', instance=g1)
MEvent.objects.create(name = 'A group event', instance=g1)
MEvent.objects.create(name = 'A group event', instance=g2)

print("Events for group 1:")
for event in list(
  MEvent.objects.events_for_object(g1)
):
  print(f"  - {event}")

print("Events for group 2:")
for event in list(
  MEvent.objects.events_for_object(g2)
):
  print(f"  - {event}")