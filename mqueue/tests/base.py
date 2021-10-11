from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from mqueue.models import MEvent


class MqueueBaseTest(TestCase):
    user: User

    def setUp(self):
        self.factory = RequestFactory()
        self.maxDiff = None
        self.user = User.objects.create_user(  # type: ignore
            "myuser", "myemail@test.com", "super_password"
        )

    def reset(self):
        for event in MEvent.objects.all():
            event.delete()

    def create_mevent(
        self,
        name: str = "M event",
        url: str = "/",
        obj_pk: int = 1,
        notes: str = "Notes",
    ):
        self._content_type = ContentType.objects.get_for_model(User)
        return MEvent.objects.create(
            name=name,
            url=url,
            obj_pk=obj_pk,
            notes=notes,
            model=User,
            content_type=self._content_type,
        )
