from unittest.mock import patch
from .base import MqueueBaseTest
from mqueue.watchers import (
    send_msg,
    login_action,
    logout_action,
    login_failed,
    init_watchers,
)


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
        login_failed("test", "user")

    @patch("django.contrib.auth.signals.user_logged_in")
    def test_init_watchers_login(self, mock):
        with self.settings(MQUEUE_WATCH=["login", "logout", "login_failed"]):
            init_watchers("login")
            """credentials = {'username': 'testuser', 'password': 'secret'}
            User.objects.create_user(**credentials)
            self.client.login(username='testuser', password='secret')
            self.assertTrue(mock.called)
            self.assertEqual(mock.call_count, 1)"""
