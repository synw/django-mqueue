# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from mqueue.models import MEvent


class MqueueTest(TestCase):
    
    def create_mevent(self, name="M event", url='/', obj_pk=1, notes='Notes'):
        self._content_type = ContentType.objects.get_for_model(User)
        return MEvent.objects.create(name=name, url=url, obj_pk=obj_pk, notes=notes, model=User, content_type=self._content_type)
    
    def test_mevent_creation(self):
        mevent = self.create_mevent()
        self.assertTrue(isinstance(mevent, MEvent))
        self.assertEqual(mevent.content_type, self._content_type)
        self.assertEqual(mevent.url, "/")
        self.assertEqual(mevent.name, "M event")
        self.assertEqual(mevent.obj_pk, 1)
        self.assertEqual(mevent.notes, "Notes")
        self.assertEqual(mevent.__unicode__(), unicode(mevent.name+' - '+str(mevent.date_posted)))
        return
        
    def test_create_mevent_empty(self):
        self.assertRaises(ValueError, MEvent.objects.create, 'name')
        return
    
    def test_mevent_creation_with_instance(self):
        self._content_type = ContentType.objects.get_for_model(User)
        user = User.objects.create_user('myuser', 'myemail@test.com', 'super_password')
        mevent = MEvent.objects.create(name='M Event', instance=user)
        self.assertTrue(isinstance(mevent, MEvent))
        self.assertEqual(mevent.content_type, self._content_type)
        self.assertEqual(mevent.obj_pk, 1)
        return
    
    def test_managers(self):
        user = User.objects.create_user('myuser', 'myemail@test.com', 'super_password')
        mevent1 = MEvent.objects.create(name="event1", model=User)
        mevent2 = MEvent.objects.create(name="event2", instance=user)
        self.assertEqual(list(MEvent.objects.events_for_model(User)), [mevent2, mevent1])
        self.assertEqual(MEvent.objects.count_for_model(User), 2)
        self.assertEqual(list(MEvent.objects.events_for_object(user)), [mevent2])
        return
    
    def test_managers_with_event_class(self):
        user = User.objects.create_user('myuser', 'myemail@test.com', 'super_password')
        mevent1 = MEvent.objects.create(name="event1", model=User, event_class="class1")
        mevent2 = MEvent.objects.create(name="event2", instance=user, event_class="class2")
        self.assertEqual(list(MEvent.objects.events_for_model(User, event_classes=["class1"] )), [mevent1])
        self.assertEqual(MEvent.objects.count_for_model(User, event_classes=["class2"]), 1)
        self.assertEqual(list(MEvent.objects.events_for_object(user)), [mevent2])
        return
        


