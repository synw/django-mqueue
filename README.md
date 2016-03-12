# Django Mqueue

[![Build Status](https://travis-ci.org/synw/django-mqueue.svg?branch=master)](https://travis-ci.org/synw/django-mqueue)

Simple events queueing application for Django: can be used for moderation or monitoring or loging.
Events can be linked to a model instance and a user instance.

## Install

`pip install django-mqueue`, then add `mqueue` to installed_apps and run migrations.

### Usage

There is two ways to use it:

**Events manager** : you can plug mqueue into your app by creating a mevent whenever you need. 
It can be in the save method of a model or in a form_valid method of a view for example.

  ```python
from mqueue.models import MEvent
from myapp.models import MyModel

#~ full event
MEvent.objects.create(
					model = MyModel, 
					name = obj.title, 
					obj_pk = obj.pk, 
					user = request.user,
					url = '/anything/'+obj.slug+'/', 
					admin_url = '/admin/app/model/'+str(obj.pk)+'/', 
					notes = 'Object X was saved!', 
					event_class = 'Info'
					)

#~ simpliest event
MEvent.objects.create(name = 'Something happened!')
  ```

The only required field is `name`

**Monitored Model** :

If you want a model to be automaticaly monitored you can inherit from `MonitoredModel`. This creates events
via signals for all the inherited monitored models every time an instance is created or deleted.

   ```python
from django.db import models
from mqueue.models import MonitoredModel

#~ for an existing model replace class MyModel(models.Model) by this:
class MyModel(MonitoredModel):
	# ...
  ```

:pencil2: Note: no migration is needed for an existing model, just plug and play.

To record also every save of a model instance replace `MonitoredModel` by `HighlyMonitoredModel`

### Settings

#### Event classes 

You can define your custom set of event classes and the corresponding css classes to 
display in the admin. The default values are:

  ```python
MQUEUE_EVENT_CLASSES = {
                 #~ 'Event class label' : 'css class to apply',
                'Default' : 'label label-default',
                'Important' : 'label label-primary',
                'Ok' : 'label label-success',
                'Info' : 'label label-info',
                'Debug' : 'label label-warning',
                'Warning' : 'label label-danger',
                'Error' : 'label label-danger',
                'Object created' : 'label label-primary',
                'Object edited' : 'label label-info',
                'Object deleted' : 'label label-warning',
                }
  ```

Note: if the `event_class` field value is not in MQUEUE_EVENT_CLASSES, the display will fallback to the 'Default' css.
 
![Event classes](https://raw.github.com/synw/django-mqueue/master/docs/img/events_list.png)
 
To use your own event classes set a `MQUEUE_EVENT_CLASSES` setting. Ex:
  
  ```python
MQUEUE_EVENT_CLASSES = {
				#~ 'Event class label' : 'css class to apply',
				'Default' : 'mydefaultcssclass',
                'User registered' : 'mycssclass',
                'Post reviewed' : 'mycssclass mycssclass2',
                'Error in some process' : 'mycssclass mycssclass2',
                #~ keep those for monitored models
                'Object created' : 'mycssclass',
                'Object edited' : 'mycssclass',
                'Object deleted' : 'mycssclass',
                # ...
                }
  ```
  
 Note: if an `event_class` that is not in is MQUEUE_EVENT_CLASSES is provided during event creation the first 
 tuple will be used for formating.
 
 You can also extend the default event classes:
 
  ```python
from mqueue.conf import EVENT_CLASSES
extra_classes = {
                'User registered' : 'mycssclass1',
                'Post reviewed' : 'mycssclass1 mycssclass2',
                'Error in some process' : 'mycssclass1 mycssclass2',
                # ...
                }
MQUEUE_EVENT_CLASSES = dict(EVENT_CLASSES, **extra_classes)
  ``` 
 
#### Event Icons
 
 You can provide html for displaying icons in your `event_class`. The defaults are:
 
  ```python
EVENT_ICONS_HTML = {
                 #~ 'Event class lable' : 'icon css class',
                'Default' : '<span class="label label-default"></span>',
                'Important' : '<span class="glyphicon glyphicon-star"></span>',
                'Ok' : '<span class="glyphicon glyphicon-ok"></span>',
                'Info' : '<span class="glyphicon glyphicon-hand-right"></span>',
                'Debug' : '<span class="glyphicon glyphicon-cog"></span>',
                'Warning' : '<span class="glyphicon glyphicon-exclamation-sign"></span>',
                'Error' : '<span class="glyphicon glyphicon-alert"></span>',
                'Object edited' : '<span class="glyphicon glyphicon-pencil"></span>',
                'Object created' : '<span class="glyphicon glyphicon-download-alt"></span>',
                'Object deleted' : '<span class="glyphicon glyphicon-remove"></span>',
                }
  ``` 
 
 Extend it the same way as MQUEUE_EVENT_CLASSES
 
#### Event Extra html
  
You can add some extra html that will display after the event_class display:

  ```python
EVENT_EXTRA_HTML = {
                 #~ 'Event class lable' : 'html to apply',
                'My event' : ' <span class="label label-danger">!!</span>',
                } 
  ```
 
#### Stop model monitoring
 
:pencil2: If you want to switch off monitoring for some models add a setting MQUEUE_STOP_MONITORING with the names of the models:
 
   ```python
MQUEUE_STOP_MONITORING = ['Model1', 'Model2']
  ```




 

