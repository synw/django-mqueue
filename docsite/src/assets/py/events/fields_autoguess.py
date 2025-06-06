import json
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from mqueue.models import MEvent

user, _  = User.objects.get_or_create(username="someuser", password="xxxyyyzzz")

MEvent.objects.create(name = 'A user event', instance=user, bucket="autoguess_test")

for event in list(
  MEvent.objects.events_for_model(User).filter(bucket="autoguess_test")
):
  print(json.dumps(model_to_dict(event), indent=4))