from unittest.mock import patch
from django.test import TestCase
from .base import MqueueBaseTest
from django.contrib.auth.models import User
from mqueue.models import MEvent
from mqueue.tracking import mqueue_tracker
from mqueue.signals import mmessage_create


class MqueueTestSignals(MqueueBaseTest):

    def test_register(self):
        mqueue_tracker.register(User, ["c"])
        mqueue_tracker.register(User, ["u"])
        mqueue_tracker.register(User, ["d"])

    """
    TOFIX

    @patch('mqueue.signals.mmessage_create')
    def test_signal_create(self, mock):
        mqueue_tracker.register(User, ["c", "u", "d"])
        User.objects.create_user(
            'myuser2', 'myemail2@test.com', 'super_password')
        self.assertTrue(mock.called)
        self.assertEqual(mock.call_count, 1)

    """
