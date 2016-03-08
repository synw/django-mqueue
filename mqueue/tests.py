# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from mqueue.models import MEvent


class MqueueTest(TestCase):
    content_type = ContentType.objects.get_for_model(MEvent)
    
    def create_mevent(self, name="M event", url='/', obj_pk=1, notes='Notes'):
        return MEvent.objects.create(name=name, url=url, obj_pk=obj_pk, notes=notes, content_type=self.content_type)
    
    def test_mevent_creation(self):
        mevent = self.create_mevent()
        self.assertTrue(isinstance(mevent, MEvent))
        self.assertEqual(mevent.content_type, self.content_type)
        self.assertEqual(mevent.url, "/")
        self.assertEqual(mevent.obj_pk, 1)
        self.assertEqual(mevent.notes, "Notes")
        self.assertEqual(mevent.__unicode__(), mevent.name)