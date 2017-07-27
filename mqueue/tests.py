# -*- coding: utf-8 -*-

from django.db import models
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django_fake_model import models as f
from mqueue.models import MEvent
from mqueue.utils import get_event_class_str, get_object_name, get_url, format_event_class
from mqueue.conf import EVENT_CLASSES, EVENT_ICONS_HTML


class FakeModel(f.FakeModel):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return "http://absoluteurl"


class FakeModelTitle(f.FakeModel):
    title = models.CharField(max_length=100)

    def get_event_object_url(self):
        return "http://eventurl"


class FakeModelSlug(f.FakeModel):
    slug = models.SlugField()


class FakeModelEmpty(f.FakeModel):
    pass


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
        self.assertEqual(mevent.__unicode__(), unicode(
            mevent.name + ' - ' + str(mevent.date_posted)))
        return

    def test_create_mevent_empty(self):
        self.assertRaises(ValueError, MEvent.objects.create, 'name')
        return

    def test_mevent_creation_with_instance(self):
        self._content_type = ContentType.objects.get_for_model(User)
        user = User.objects.create_user(
            'myuser', 'myemail@test.com', 'super_password')
        mevent = MEvent.objects.create(name='M Event', instance=user)
        self.assertTrue(isinstance(mevent, MEvent))
        self.assertEqual(mevent.content_type, self._content_type)
        self.assertEqual(mevent.obj_pk, 1)
        return

    def test_utils_get_event_class_str(self):
        event_class = "Obj created"
        self.assertEqual(get_event_class_str(event_class), "Object created")
        event_class = "Obj edited"
        self.assertEqual(get_event_class_str(event_class), "Object edited")
        event_class = "Obj deleted"
        self.assertEqual(get_event_class_str(event_class), "Object deleted")
        event_class = None
        self.assertEqual(get_event_class_str(event_class), "Default")

    @FakeModel.fake_me
    @FakeModelTitle.fake_me
    @FakeModelSlug.fake_me
    @FakeModelEmpty.fake_me
    def test_utils_get_object_name(self):
        # test unicode method
        instance, created = MEvent.objects.get_or_create(name="Event name")
        user = User.objects.create_user(
            'myuser', 'myemail@test.com', 'super_password')
        object_name = get_object_name(instance, user)
        res = instance.__class__.__name__ + ' ' + \
            instance.__unicode__()[:45] + '...' + ' (' + user.username + ')'
        self.assertEqual(object_name, res)
        # test name
        FakeModel.objects.create(name='123')
        instance = FakeModel.objects.get(name='123')
        res = instance.__class__.__name__ + ' ' + \
            instance.name + ' (' + user.username + ')'
        object_name = get_object_name(instance, user)
        self.assertEqual(object_name, res)
        # test title
        FakeModelTitle.objects.create(title='123')
        instance = FakeModelTitle.objects.get(title='123')
        res = instance.__class__.__name__ + ' ' + \
            instance.title + ' (' + user.username + ')'
        object_name = get_object_name(instance, user)
        self.assertEqual(object_name, res)
        # test slug
        FakeModelSlug.objects.create(slug='123')
        instance = FakeModelSlug.objects.get(slug='123')
        res = instance.__class__.__name__ + ' ' + \
            instance.slug + ' (' + user.username + ')'
        object_name = get_object_name(instance, user)
        self.assertEqual(object_name, res)
        # test pk
        instance, created = FakeModelEmpty.objects.get_or_create()
        res = instance.__class__.__name__ + ' ' + \
            str(instance.pk) + ' (' + user.username + ')'
        object_name = get_object_name(instance, user)
        self.assertEqual(object_name, res)

    @FakeModel.fake_me
    @FakeModelTitle.fake_me
    def test_utils_get_url(self):
        # test from absolute url
        instance, created = FakeModel.objects.get_or_create(name='123')
        url = get_url(instance)
        self.assertEqual(url, "http://absoluteurl")
        # test from custom method
        instance, created = FakeModelTitle.objects.get_or_create(title='123')
        url = get_url(instance)
        self.assertEqual(url, "http://eventurl")

    def test_utils_format_event_class(self):
        # test with obj
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class="Default")
        event_class_formated = format_event_class(instance)
        icon = EVENT_ICONS_HTML[instance.event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[instance.event_class] + '">' + \
            icon + instance.event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        # test with event_class
        event_class = "Default"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        icon = EVENT_ICONS_HTML[event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[event_class] + '">' + icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        event_class = "Myobj created"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = 'Object created'
        icon = EVENT_ICONS_HTML[res_event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[res_event_class] + '">' + \
            icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        event_class = "Myobj edited"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = 'Object edited'
        icon = EVENT_ICONS_HTML[res_event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[res_event_class] + '">' + \
            icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        event_class = "Myobj deleted"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = 'Object deleted'
        icon = EVENT_ICONS_HTML[res_event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[res_event_class] + '">' + \
            icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        event_class = "Random event class"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = 'Default'
        icon = EVENT_ICONS_HTML[res_event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[res_event_class] + '">' + \
            icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        event_class = "Some error event"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = 'Error'
        icon = EVENT_ICONS_HTML[res_event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[res_event_class] + '">' + \
            icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        event_class = "Some debug event"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = 'Debug'
        icon = EVENT_ICONS_HTML[res_event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[res_event_class] + '">' + \
            icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        event_class = "Some warning event"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = 'Warning'
        icon = EVENT_ICONS_HTML[res_event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[res_event_class] + '">' + \
            icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        event_class = "Some info event"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = 'Info'
        icon = EVENT_ICONS_HTML[res_event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[res_event_class] + '">' + \
            icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        event_class = "Some important event"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class)
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = 'Important'
        icon = EVENT_ICONS_HTML[res_event_class] + '&nbsp;'
        html = '<span class="' + \
            EVENT_CLASSES[res_event_class] + '">' + \
            icon + event_class + '</span>'
        self.assertEqual(event_class_formated, html)
        # extra html


"""
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
"""
