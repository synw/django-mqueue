from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from mqueue.models import MEvent


class MqueueBaseTest(TestCase):
    user = None

    def setUp(self):
        self.factory = RequestFactory()
        self.maxDiff = None
        self.user = User.objects.create_user(
            'myuser', 'myemail@test.com', 'super_password')

    def reset(self):
        for event in MEvent.objects.all():
            event.delete()

    def create_mevent(self, name="M event", url='/', obj_pk=1, notes='Notes'):
        self._content_type = ContentType.objects.get_for_model(User)
        return MEvent.objects.create(name=name, url=url, obj_pk=obj_pk, notes=notes,
                                     model=User, content_type=self._content_type)
