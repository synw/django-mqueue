from django.test import TestCase
from .base import MqueueBaseTest
from mqueue.models import MEvent
from mqueue.watchers import send_msg, login_action, logout_action, login_failed, init_watchers
from mqueue.conf import WATCH


class MqueueTestWatchers(MqueueBaseTest):

    def test_send_msg(self):
        instance = self.user
        send_msg("test", instance, "Event string")

    def test_login_action(self):
        instance = self.user
        login_action("test", instance)

    def test_logout_action(self):
        instance = self.user
        logout_action("test", instance)

    def test_login_failed(self):
        instance = self.user
        login_failed("test", "user")

    def test_init_watchers_login(self):
        with self.settings(MQUEUE_WATCH=["login", "logout", "login_failed"]):
            init_watchers("login")
