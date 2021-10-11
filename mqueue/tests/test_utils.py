from .base import MqueueBaseTest
from mqueue.models import MEvent
from mqueue.utils import (
    get_event_class_str,
    get_object_name,
    format_event_class,
)
from mqueue.conf import EVENT_CLASSES, EVENT_ICONS_HTML


class MqueueTestUtils(MqueueBaseTest):
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
        res: str = (
            instance.__class__.__name__
            + " - "
            + str(instance.date_posted)
            + " ("
            + user.username  # type: ignore
            + ")"
        )
        self.assertEqual(object_name, res)
        # test name
        MEvent.objects.create(name="123")
        instance = MEvent.objects.get(name="123")
        res: str = (
            instance.__class__.__name__
            + " - "
            + str(instance.date_posted)
            + " ("
            + user.username  # type: ignore
            + ")"
        )
        object_name = get_object_name(instance, user)
        self.assertEqual(object_name, res)
        self.reset()

        # app = MqueueConfig("mqueue", mqueue)
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
            name="Event name", event_class="Default"
        )
        event_class_formated = format_event_class(instance)
        icon = EVENT_ICONS_HTML[instance.event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[instance.event_class]
            + '">'
            + icon
            + instance.event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        # test with event_class
        event_class = "Default"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        icon = EVENT_ICONS_HTML[event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        event_class = "Object created"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = "Object created"
        icon = EVENT_ICONS_HTML[res_event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[res_event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        event_class = "Object edited"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = "Object edited"
        icon = EVENT_ICONS_HTML[res_event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[res_event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        event_class = "Object deleted"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = "Object deleted"
        icon = EVENT_ICONS_HTML[res_event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[res_event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        """event_class = "Random event class"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = "Default"
        icon = EVENT_ICONS_HTML[res_event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[res_event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        event_class = "Error"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = "Error"
        icon = EVENT_ICONS_HTML[res_event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[res_event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        event_class = "Debug"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = "Debug"
        icon = EVENT_ICONS_HTML[res_event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[res_event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        event_class = "Warning"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = "Warning"
        icon = EVENT_ICONS_HTML[res_event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[res_event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        event_class = "Info"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = "Info"
        icon = EVENT_ICONS_HTML[res_event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[res_event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)
        event_class = "Important"
        instance, created = MEvent.objects.get_or_create(
            name="Event name", event_class=event_class
        )
        event_class_formated = format_event_class(event_class=event_class)
        res_event_class = "Important"
        icon = EVENT_ICONS_HTML[res_event_class] + "&nbsp;"
        html = (
            '<span class="'
            + EVENT_CLASSES[res_event_class]
            + '">'
            + icon
            + event_class
            + "</span>"
        )
        self.assertEqual(event_class_formated, html)"""
