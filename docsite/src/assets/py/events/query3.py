from mqueue.models import MEvent

MEvent.objects.create(
  name = 'An event',
  event_class="Info",
  bucket="bucket1",
  data= [1, 2],
  notes="special"
)

events = MEvent.objects.filter(
  event_class="Info",
  bucket="bucket1",
  notes="special"
)

event = events[0]
print(f"  - {event.event_class} {event.name} {event.data}")