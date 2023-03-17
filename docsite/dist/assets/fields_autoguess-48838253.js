import{d as o,a as n,b as a,f as r,q as s,u as e,D as l,E as d,H as i,O as u,G as t}from"./index-22118213.js";const c=`import json
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from mqueue.models import MEvent

user, _  = User.objects.get_or_create(username="someuser", password="xxxyyyzzz")

MEvent.objects.create(name = 'A user event', instance=user, bucket="autoguess_test")

for event in list(
  MEvent.objects.events_for_model(User).filter(bucket="autoguess_test")
):
  print(json.dumps(model_to_dict(event), indent=4))`,m=`from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

class MyModel(models.Model):
    name = models.CharField(max_length=120)
    user = models.ForeignKey(
        USER_MODEL,
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    def get_event_object_url(self) -> str:
        return f"/some/url/{self.name}"
`,p={class:"prosed"},_=t('<h1>Fields autoguess</h1><p>If you provided an instance or a content_type and a model mqueue will guess the following fields unless you provided arguments for:</p><ul><li><kbd>content_type</kbd> <span class="var">ContentType</span> the content type of the associated object</li><li><kbd>obj_pk</kbd> <span class="var">int</span> the primary key of the object</li><li><kbd>admin_url</kbd> <span class="var">str</span> will be reversed from the instance</li><li><kbd>user</kbd> <span class="var">User</span> checks if you model has a <i>user</i> field or an <i>editor</i> field and populates from it</li><li><kbd>url</kbd> <span class="var">str</span> checks for a <i>get_event_object_url()</i> method in your model, and then check for a <i>get_absolute_url()</i> method and populates from it. Write your own <i>get_event_object_url()</i> method in your model to manage which url will be associated to the object.</li></ul><h3>Example</h3>',4),h={class:"not-prose"},f=t("<h2>Model fields</h2><p>The <kbd>user</kbd> event property can use custom model field to guess it&#39;s values. If the model has a <i>user</i> or <i>editor</i> field it will be used to fill the <kbd>user</kbd> for the event if not provided as event parameter</p><p>The <kbd>url</kbd> event property can use a custom <i>get_event_object_url()</i> or <i>get_absolute_url()</i> model method to guess it&#39;s values </p>",3),y=o({__name:"fields_autoguess",setup(b){return(g,k)=>(n(),a("div",p,[_,r("p",h,[s(e(d),{id:"1",code:e(c),py:e(l),namespace:"codeblock",class:"w-limited"},null,8,["code","py"])]),f,s(e(u),{hljs:e(i),code:e(m),lang:"python",class:"not-prose"},null,8,["hljs","code"])]))}});export{y as default};
