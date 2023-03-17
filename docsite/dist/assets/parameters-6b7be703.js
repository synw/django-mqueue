import{d as s,a,b as t,f as n,q as o,u as e,H as l,O as r,G as i}from"./index-22118213.js";const d=`from mqueue.models import MEvent
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
)`,p={class:"prosed"},c=i('<h1>Create events</h1><h2>Parameters</h2><ul><li><kbd>name</kbd> <span class="var">str</span> the event short name <b>required</b></li><li><kbd>bucket</kbd> <span class="var">str</span> the event bucket name</li><li><kbd>data</kbd> <span class="var">Dict | List</span> some json data associated with the event</li><li><kbd>scope</kbd> <span class="var">Literal[&quot;public&quot;, &quot;users&quot;, &quot;staff&quot;, &quot;superuser&quot;]</span> the event scope. Possible values are: <i>public</i>, <i>users</i>, <i>staff</i> and <i>superuser</i>. Defaults to <i>superuser</i></li><li><kbd>event_class</kbd> <span class="var">str</span> the event class</li><li><kbd>model</kbd> <span class="var">models.Model</span> a Django model</li><li><kbd>obj_pk</kbd> <span class="var">int</span> the foreign key of an object</li><li><kbd>instance</kbd> <span class="var">models.Model instance</span> an instance of a Django model. This parameter will not be recorded: it is only used for auto guessing some fields.</li><li><kbd>user</kbd> <span class="var">User</span> an instance of a user model</li><li><kbd>url</kbd> <span class="var">str</span> an url associated with the event</li><li><kbd>admin_url</kbd> <span class="var">str</span> an admin url associated with the event</li><li><kbd>notes</kbd> <span class="var">str</span> a text associated with the event</li><li><kbd>request</kbd> <span class="var">HttpRequest</span> a request associated with the event</li><li><kbd>groups</kbd> <span class="var">List[Group]</span> a list of groups associated with the event</li></ul><h3>Example with all parameters</h3>',4),u={class:"not-prose"},v=s({__name:"parameters",setup(b){return(k,m)=>(a(),t("div",p,[c,n("p",u,[o(e(r),{code:e(d),hljs:e(l),lang:"python"},null,8,["code","hljs"])])]))}});export{v as default};
