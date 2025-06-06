from mqueue.models import MEvent
from myapp.models import MyModel

obj = MyModel.objects.get(x="y")

MEvent.objects.create(
   name = obj.title,
   event_class = 'Info',
   bucket = "bucket_name",
   data = {"foo": "bar"},
   scope = "users",
   model = MyModel,
   obj_pk =obj.pk,
   instance = obj,
   user = request.user,
   url ='/anything/'+obj.slug+'/',
   admin_url ='/admin/app/model/'+str(obj.pk)+'/',
   notes = 'Object X was saved!',
   request = request,
   groups = [group1]
)