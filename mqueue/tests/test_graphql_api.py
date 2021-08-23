"""
from .base import MqueueBaseTest
from graphene.test import Client
from mqueue.schema import schema
from mqueue.models import MEvent


client = Client(schema)


class MqueueTestGraphqlApi(MqueueBaseTest):

    ""
    # TOFIX
    def test_graphql_query(self):
        self.reset()
        MEvent.objects.create(name="Test public event", scope="public")
        query = '''query publicEvents(first:10) {
                edges {
                    node {
                        name
                        event_class
                    }
                }
            }
        '''
        res = [{"name": "Test public event"}]
        self.assertEqual(client.execute(query), res)
"""
