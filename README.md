# Django Mqueue

[![Build Status](https://travis-ci.org/synw/django-mqueue.svg?branch=master)](https://travis-ci.org/synw/django-mqueue)

Simple events queueing application for Django: can be used for moderation or monitoring or loging.
Events are linked to a model instance.

## Install

`pip install django-mqueue`, then add `mqueue` to installed_apps and run migrations.

### Usage

**Events manager** : you can plug mqueue into your app by creating a mevent whenever you need. 
It can be in the save method of a model or in a form_valid method of a view for example.

  ```python
from mqueue.models import MEvent
from myapp.models import MyModel

MEvent.events.create(
					model = MyModel, 
					name = obj.title, 
					obj_pk = obj.pk, 
					url = '/anything/'+obj.slug+'/', 
					admin_url = '/admin/app/model/'+str(obj.pk)+'/', 
					notes = 'Object X was saved!', 
					event_class = 'Info'
					)
  ```

The only required field is `name`

**Monitored Model** :

If you want a model to be automaticaly monitored you can inherit from `MonitoredModel`. This creates events
via a signals for all the inherited monitored models every time an instance is created or deleted.

   ```python
from django.db import models
from mqueue.models import MonitoredModel

class MyModel(MonitoredModel):
	# ...
  ```

:pen: Note: no migration is needed, just plug and play.

### Settings

**Event classes**: you can define your custom set of event classes and the corresponding css classes to 
display in the admin. The default values are:

  ```python
MQUEUE_EVENT_CLASSES = {
                 #~ 'Envent label' : 'css class to apply',
                'Default' : 'label label-default',
                'Important' : 'label label-primary',
                'Ok' : 'label label-success',
                'Info' : 'label label-info',
                'Debug' : 'label label-warning',
                'Warning' : 'label label-danger',
                'Error' : 'label label-danger',
                'Object created' : 'label label-primary',
                'Object deleted' : 'label label-warning',
                }
  ```

Note: if the `event_class` field is empty, the display will fallback to the 'Default' css.
 
![Event classes](https://raw.github.com/synw/django-mqueue/master/docs/img/events_list.png)
 
To use your own event classes customize the `MQUEUE_EVENT_CLASSES` setting. Ex:
  
  ```python
MQUEUE_EVENT_CLASSES = {
				'Default' : 'mydefaultcssclass',
                'User registered' : 'mycssclass1',
                'Post reviewed' : 'mycssclass1 mycssclass2',
                'Error in some process' : 'mycssclass1 mycssclass2',
                # ...
                }
  ```
 
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
 
 Note: if an `event_class` that is not in is MQUEUE_EVENT_CLASSES is provided during event creation the first 
 tuple will be used as default. 
 
 :pen: To stop monitoring a MonitoredModel add a setting MQUEUE_STOP_MONITORING with the names of the models:
 
   ```python
MQUEUE_STOP_MONITORING = ['Model1', 'Model2']
  ```




 

