from  django.utils import timezone
from mqueue.models import MEvent

now = timezone.now()
MEvent.objects.create(name = 'Event now')
events = MEvent.objects.filter(date_posted__gte=now)
for event in events:
    print(event)