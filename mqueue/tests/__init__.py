from .admin import MqueueTestAdmin
from .create import MqueueTestCreate
from .managers import MqueueTestManagers
from .apps import MqueueTestApps
from .utils import MqueueTestUtils
from .hooks.redis import MqueueTestRedisHook
from .watchers import MqueueTestWatchers
from .signals import MqueueTestSignals
#from .graphql_api import MqueueTestGraphqlApi


class MqueueTest(MqueueTestAdmin,
                 MqueueTestCreate,
                 MqueueTestManagers,
                 MqueueTestApps,
                 MqueueTestUtils,
                 MqueueTestWatchers,
                 # MqueueTestGraphqlApi
                 ):

    def test_mqueue_logging(self):
        from mqueue.logging import DEV_LOGGING, LOGGING_WARNING
