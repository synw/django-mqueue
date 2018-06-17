from django.test import TestCase
from .base import MqueueBaseTest
from django.contrib.auth.models import User
from mqueue.models import MEvent


class MqueueTestManagers(MqueueBaseTest):

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
