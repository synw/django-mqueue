# Django Moderation Queue

Simple moderation queue application for Django

## Install

Clone, add `mqueue` to installed_apps and run migrations

## Usage

You need to plug mqueue into your app by creating a moderated event whenever you need. It can be in the save method of a model or in a form_valid method of a view for example.

  ```python
from django.contrib.contenttypes.models import ContentType
from mqueue.models import ModerationEvent

content_type = ContentType.objects.get_for_model(MyModel)
url = '/anything/'+obj.slug+'/' # for example
note = 'Object X was saved!'
ModerationEvent.objects.create(name=obj.title, content_type=content_type, url=url, notes=notes, obj_pk = obj.pk)
  ```
Note: `name`, `content_type`, `obj_pk` and `url` are required fields

Then go to the admin to see your moderation queue.
