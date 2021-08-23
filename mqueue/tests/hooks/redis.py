"""from mqueue.tests.base import MqueueBaseTest
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from mqueue.models import MEvent
from mqueue import hooks
from mqueue.hooks.redis.serializer import Pack


class MqueueTestRedisHook(MqueueBaseTest):
    def test_init_hooks(self):
        mevent = self.create_mevent()
        hooks.dispatch(mevent)

    def test_redis_serializer(self):
        request = self.factory.get("/")
        ct = ContentType.objects.get_for_model(User)
        user = self.user
        mevent = MEvent.objects.create(
            name="Event",
            user=user,
            content_type=ct,
            event_class="test",
            data={"k": "v"},
            url="http://event",
            admin_url="http://admin",
            bucket="test",
            request=request,
            notes="xx",
            instance=user,
        )
        data = Pack(mevent)
        mevent.request = mevent.request.replace("\n", "//")
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
        mevent = MEvent.objects.create(name="Event")
        res = "name:;" + mevent.name
        data = Pack(mevent)
        self.assertEqual(data, res)
"""
