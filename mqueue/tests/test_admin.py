from django.contrib import admin
from .base import MqueueBaseTest
from mqueue.models import MEvent
from mqueue.admin import link_to_object, link_to_object_admin, MEventAdmin


class MqueueTestAdmin(MqueueBaseTest):
    def test_admin(self):
        instance, _ = MEvent.objects.get_or_create(
            name="Event name", url="http://url", admin_url="http://admin_url"
        )
        res = link_to_object(instance)
        link = '<a href="http://url" target="_blank">http://url</a>'
        self.assertEqual(link, res)
        res = link_to_object_admin(instance)
        link = '<a href="http://admin_url" target="_blank">http://admin_url</a>'
        self.assertEqual(link, res)
        request = self.factory.get("/")

        class TestAdminSite(admin.AdminSite):
            pass

        adm = MEventAdmin(MEvent, TestAdminSite)
        res = adm.get_readonly_fields(request)
        self.assertEqual(res, ("notes", "request"))
