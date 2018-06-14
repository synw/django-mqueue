# -*- coding: utf-8 -*-

from django.db import models
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib import admin
#from django.apps import AppConfig
from mqueue.models import MEvent
from mqueue.utils import get_event_class_str, get_object_name, get_url, format_event_class
from mqueue.conf import EVENT_CLASSES, EVENT_ICONS_HTML
from mqueue.hooks.redis.serializer import Pack
from mqueue.hooks import redis
from mqueue import logging
from mqueue.apps import MqueueConfig
from mqueue.admin import link_to_object, link_to_object_admin, MEventAdmin


class MqueueTest(TestCase):
    user = None

    def setUp(self):
        self.factory = RequestFactory()
        self.maxDiff = None
        self.user = User.objects.create_user(
            'myuser', 'myemail@test.com', 'super_password')

    def create_mevent(self, name="M event", url='/', obj_pk=1, notes='Notes'):
        self._content_type = ContentType.objects.get_for_model(User)
        return MEvent.objects.create(name=name, url=url, obj_pk=obj_pk, notes=notes,
                                     model=User, content_type=self._content_type)

    def reset(self):
        for event in MEvent.objects.all():
            event.delete()

    def test_mevent_creation(self):
        mevent = self.create_mevent()
        self.assertTrue(isinstance(mevent, MEvent))
        self.assertEqual(mevent.content_type, self._content_type)
        self.assertEqual(mevent.url, "/")
        self.assertEqual(mevent.name, "M event")
        self.assertEqual(mevent.obj_pk, 1)
        self.assertEqual(mevent.notes, "Notes")
        self.assertEqual(mevent.__unicode__(), mevent.name +
                         ' - ' + str(mevent.date_posted))

    def test_create_mevent_empty(self):
        self.assertRaises(ValueError, MEvent.objects.create, 'name')

    def test_mevent_creation_with_user(self):
        self._content_type = ContentType.objects.get_for_model(User)
        self.reset()
        user = self.user
        mevent = MEvent.objects.create(
            name='M Event', instance=user, user=user)
        self.assertTrue(isinstance(mevent, MEvent))
        self.assertEqual(mevent.content_type, self._content_type)
        self.assertEqual(mevent.obj_pk, 1)
        self.assertEqual(mevent.user, user)
        self.reset()

    def test_event_creation_more(self):
        request = self.factory.get('/')
        mevent = MEvent.objects.create(
            name='123',
            scope="superuser",
            bucket="sup",
            request=request,
            data={"k": "v"},
            admin_url="http://admin",
        )
        self.assertTrue(isinstance(mevent, MEvent))
        self.assertEqual(mevent.name, "123")
        self.assertEqual(mevent.scope, "superuser")
        self.assertEqual(mevent.bucket, "sup")
        self.assertEqual(mevent.admin_url, "http://admin")
        formated_request = ""
        for key in request.META.keys():
            formated_request += str(key) + ' : ' + \
                str(request.META[key]) + '\n'
        self.assertEqual(mevent.request, formated_request)
        self.assertEqual(mevent.data, {"k": "v"})

    def test_utils_get_event_class_str(self):
        event_class = "Obj created"
        self.assertEqual(get_event_class_str(event_class), "Object created")
        event_class = "Obj edited"
        self.assertEqual(get_event_class_str(event_class), "Object edited")
        event_class = "Obj deleted"
        self.assertEqual(get_event_class_str(event_class), "Object deleted")
        event_class = None
        self.assertEqual(get_event_class_str(event_class), "Default")

    def test_utils_get_object_name(self):
        self.reset()
        # test unicode method
        instance, _ = MEvent.objects.get_or_create(name="Event name")
        user = self.user
        object_name = get_object_name(instance, user)
        res = instance.__class__.__name__ + ' - ' + \
            str(instance.date_posted) + ' (' + user.username + ')'
        self.assertEqual(object_name, res)
        # test name
        MEvent.objects.create(name='123')
        instance = MEvent.objects.get(name='123')
        res = instance.__class__.__name__ + ' - ' + \
            str(instance.date_posted) + ' (' + user.username + ')'
        object_name = get_object_name(instance, user)
        self.assertEqual(object_name, res)
        self.reset()

    def test_admin(self):
        instance, _ = MEvent.objects.get_or_create(name="Event name",
                                                   url="http://url",
                                                   admin_url="http://admin_url")
        res = link_to_object(instance)
        link = '<a href="http://url" target="_blank">http://url</a>'
        self.assertEqual(link, res)
        res = link_to_object_admin(instance)
        link = '<a href="http://admin_url" target="_blank">http://admin_url</a>'
        self.assertEqual(link, res)
        request = self.factory.get('/')

        class TestAdminSite(admin.AdminSite):
            pass

        adm = MEventAdmin(MEvent, TestAdminSite)
        res = adm.get_readonly_fields(request)
        self.assertEqual(res, ('notes', 'request'))

    def test_apps(self):
        pass
        #app = MqueueConfig("mqueue", mqueue)
        # app.ready()

    """def test_utils_get_url(self):
        # test from absolute url
        instance, created = MEvent.objects.get_or_create(name='123')
        url = get_url(instance)
        self.assertEqual(url, "http://absoluteurl")
        # test from custom method
        instance, created = MEvent.objects.get_or_create(title='123')
        url = get_url(instance)
        self.assertEqual(url, "http://eventurl")"""

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

    """
    Hooks
    """

    def test_redis_serializer(self):
        request = self.factory.get('/')
        ct = ContentType.objects.get_for_model(User)
        user = self.user
        mevent = MEvent.objects.create(
            name='Event', user=user, content_type=ct,
            event_class="test", data={"k": "v"}, url="http://event",
            admin_url="http://admin", bucket="test", request=request,
            notes="xx", instance=user)
        data = Pack(mevent)
        ser = ["name:;" + mevent.name]
        ser.append("event_class:;" + mevent.event_class)
        ser.append("content_type:;" + str(mevent.content_type))
        ser.append("obj_pk:;" + str(mevent.obj_pk))
        ser.append("user:;" + str(mevent.user))
        ser.append("url:;" + mevent.url)
        ser.append("admin_url:;" + mevent.admin_url)
        ser.append("notes:;" + mevent.notes)
        ser.append("request:;" + mevent.request)
        ser.append("bucket:;" + mevent.bucket)
        ser.append("data:;" + str(mevent.data))
        sep = "#!#"
        res = str.join(sep, ser)
        self.assertEqual(data, res)

    def test_redis_serializer_min(self):
        mevent = MEvent.objects.create(name='Event')
        res = "name:;" + mevent.name
        data = Pack(mevent)
        self.assertEqual(data, res)

    """
    Managers
    """

    def test_managers(self):
        self.reset()
        user = self.user
        mevent1 = MEvent.objects.create(name="event1", model=User)
        mevent2 = MEvent.objects.create(name="event2", instance=user)
        self.assertEqual(
            list(
                MEvent.objects.events_for_model(User)), [
                mevent2, mevent1])
        self.assertEqual(MEvent.objects.count_for_model(User), 2)
        self.assertEqual(
            list(
                MEvent.objects.events_for_object(user)),
            [mevent2])
        return

    def test_managers_with_event_class(self):
        self.reset()
        user = self.user
        mevent1 = MEvent.objects.create(
            name="event1", model=User, event_class="class1")
        mevent2 = MEvent.objects.create(
            name="event2", instance=user, event_class="class2")
        self.assertEqual(
            list(
                MEvent.objects.events_for_model(
                    User,
                    event_classes=["class1"])),
            [mevent1])
        self.assertEqual(
            MEvent.objects.count_for_model(
                User, event_classes=["class2"]), 1)
        self.assertEqual(
            list(
                MEvent.objects.events_for_object(user)),
            [mevent2])
        return
