from mqueue.models import MEvent

MEvent.objects.create(name = 'Event 1', event_class="Info")
MEvent.objects.create(name = 'Event 2', event_class="Warning")
MEvent.objects.create(name = 'Event 3', event_class="Error")
events = MEvent.objects.all()
for event in events:
    print(event.event_class, event)