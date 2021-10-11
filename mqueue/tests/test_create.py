from .base import MqueueBaseTest
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from mqueue.models import MEvent


class MqueueTestCreate(MqueueBaseTest):
    def create_mevent(self, name="M event", url="/", obj_pk=1, notes="Notes"):
        self._content_type = ContentType.objects.get_for_model(User)
        return MEvent.objects.create(
            name=name,
            url=url,
            obj_pk=obj_pk,
            notes=notes,
            model=User,
            content_type=self._content_type,
        )

    def test_mevent_creation(self):
        mevent = self.create_mevent()
        self.assertTrue(isinstance(mevent, MEvent))
        self.assertEqual(mevent.content_type, self._content_type)
        self.assertEqual(mevent.url, "/")
        self.assertEqual(mevent.name, "M event")
        self.assertEqual(mevent.obj_pk, 1)
        self.assertEqual(mevent.notes, "Notes")
        self.assertEqual(
            mevent.__str__(), mevent.name + " - " + str(mevent.date_posted)
        )

    def test_create_mevent_empty(self):
        self.assertRaises(ValueError, MEvent.objects.create, "name")

    def test_mevent_creation_with_user(self):
        self._content_type = ContentType.objects.get_for_model(User)
        self.reset()
        user = self.user
        mevent = MEvent.objects.create(name="M Event", instance=user, user=user)
        self.assertTrue(isinstance(mevent, MEvent))
        self.assertEqual(mevent.content_type, self._content_type)
        self.assertEqual(mevent.obj_pk, 1)
        self.assertEqual(mevent.user, user)
        self.reset()

    def test_event_creation_more(self):
        request = self.factory.get("/")
        mevent = MEvent.objects.create(
            name="123",
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
            formated_request += str(key) + " : " + str(request.META[key]) + "\n"
        self.assertEqual(mevent.request, formated_request)
        self.assertEqual(mevent.data, {"k": "v"})
