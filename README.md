# Django Mqueue

[![Build Status](https://travis-ci.org/synw/django-mqueue.svg?branch=master)](https://travis-ci.org/synw/django-mqueue)

Simple events queueing application for Django: can be used for moderation or monitoring or loging.
Events are linked to a model instance.

## Install

`pip install django-mqueue`, then add `mqueue` to installed_apps and run migrations.

## Usage

You can plug mqueue into your app by creating a moderated event whenever you need. It can be in the save method of a model or in a form_valid method of a view for example.

  ```python
from django.contrib.contenttypes.models import ContentType
from mqueue.models import MEvent

content_type = ContentType.objects.get_for_model(MyModel)
url = '/anything/'+obj.slug+'/' # for example
note = 'Object X was saved!'
MEvent.objects.create(name=obj.title, content_type=content_type, url=url, notes=notes, obj_pk=obj.pk)
  ```
Note: `name`, `content_type`, `obj_pk` and `url` are required fields. The url field is used in the admin to make a link to see the object.

Then go to the admin to see your events queue.

### New in 0.3 to come (for now in master)

**Events manager** for creation, no more ContentType import is required: just pass the model to the manager.

  ```python
from mqueue.models import MEvent

url = '/anything/'+obj.slug+'/' #url for object view on site
admin_url = '/admin/app/model/'+str(obj.pk)+'/' #url for object view in admin
note = 'Object X was saved!'
MEvent.events.create(model=MyModel, name=obj.title, obj_pk=obj.pk, url=url, admin_url=admin_url, notes=notes, event_class="Info")
  ```

Note: the only required fields are now `model`, `name`, and `obj_pk`

New field: `admin_url` to get a link to the object admin page

**Feature: event classes**: you can define your custom set of event classes and the corresponding css classes to 
display in the admin. The default values are:

  ```python
MQUEUE_EVENT_CLASSES = {
                 #~ 'Envent label' : 'css class to apply',
                'Default' : 'label label-default',
                'Important' : 'label label-primary',
                'Ok' : 'label label-success',
                'Info' : 'label label-info',
                'Debug' : 'label label-warning',
                'Danger' : 'label label-danger',
                }
  ```
 
![Event classes](https://raw.github.com/synw/django-mqueue/master/docs/img/events_list.png)
 
To use your own event classes customize the `MQUEUE_EVENT_CLASSES` setting. Ex:
  
  ```python
MQUEUE_EVENT_CLASSES = {
                'User post' : 'mycssclass1',
                'Post reviewed' : 'mycssclass1 mycssclass2',
                'MyModel created' : 'mycssclass1 mycssclass2',
                # ...
                }
  ```
  

