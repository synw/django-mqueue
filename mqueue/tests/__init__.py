from .admin import MqueueTestAdmin
from .create import MqueueTestCreate
from .managers import MqueueTestManagers
from .apps import MqueueTestApps
from .utils import MqueueTestUtils
from .hooks.redis import MqueueTestRedisHook


class MqueueTest(MqueueTestAdmin,
                 MqueueTestCreate,
                 MqueueTestManagers,
                 MqueueTestApps,
                 MqueueTestUtils,
                 MqueueTestRedisHook):
    pass
