import{d as c,a as r,b as a,f as n,q as t,u as e,D as o,E as s}from"./index-22118213.js";const l=`import json
from django.forms.models import model_to_dict
from django.contrib.auth.models import Group
from mqueue.models import MEvent

MEvent.objects.create(name = 'A group event', model=Group)
MEvent.objects.create(name = 'A group event', model=Group)

for event in list(
  MEvent.objects.events_for_model(Group)
):
  print(f"- {event}")`,i=`import json
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
  print(f"  - {event}")`,p=`from mqueue.models import MEvent

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
print(f"  - {event.event_class} {event.name} {event.data}")`,m={class:"prosed"},d=n("h1",null,"Query events",-1),_=n("h2",null,"Events for model",-1),u=n("p",null,"List events for a model",-1),v={class:"not-prose"},f=n("h2",null,"Events for object",-1),b=n("p",null,"List events for an object",-1),g={class:"not-prose"},j=n("h2",null,"Classic Django queries",-1),E={class:"not-prose"},q=c({__name:"query_events",setup(h){return(M,y)=>(r(),a("div",m,[d,_,u,n("p",v,[t(e(s),{id:"1",code:e(l),py:e(o),namespace:"codeblock",class:"w-limited"},null,8,["code","py"])]),f,b,n("p",g,[t(e(s),{id:"2",code:e(i),py:e(o),namespace:"codeblock",class:"w-limited"},null,8,["code","py"])]),j,n("p",E,[t(e(s),{id:"3",code:e(p),py:e(o),namespace:"codeblock",class:"w-limited"},null,8,["code","py"])])]))}});export{q as default};
