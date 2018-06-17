from django.test import TestCase
from .base import MqueueBaseTest
from django.apps import apps


class MqueueTestApps(MqueueBaseTest):

    def test_apps(self):
        apps.get_app_config('mqueue')

    def test_apps_import_error(self):
        req = (('wrong.model.path', ["c", "d", "u"]),)
        with self.settings(MQUEUE_AUTOREGISTER=req):
            apps.get_app_config('mqueue')
            self.assertRaises(ImportError)
