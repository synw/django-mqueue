Graphql Api
===========

*New in 0.9*

It is possible to query for public events, users events and staff events.

Settings
~~~~~~~~

Install with ``pip install django-graphql-utils django-filters``

 .. highlight:: python

::

   INSTALLED_APPS += ("graphene_django", "graphql_utils",)

   GRAPHENE = {
      'SCHEMA': 'mqueue.schema.schema'
   }
   
   if DEBUG is True:
      GRAPHENE['MIDDLEWARE'] = ['graphene_django.debug.DjangoDebugMiddleware']
      
   # optional: limit number of events to be retrieved in one query (default 100):
   MQUEUE_API_MAX_EVENTS = 50
   
Urls:

::

   from django.conf import settings
   from graphene_django.views import GraphQLView
   from graphql_utils.views import TGraphQLView
   
   urlpatterns = [
    # ...
    url(r'^graphql', TGraphQLView.as_view()),
   ]
   
   if settings.DEBUG:
      urlpatterns += [url(r'^graphiql', GraphQLView.as_view(graphiql=True)), ]

Note: the ``/graphql`` endpoint is protected by a Django csrf token

Event scope
~~~~~~~~~~~

Use the ``scope`` parameter in your events to make them available to the Api:

 .. highlight:: python

::

   MEvent.objects.create(name="Test public event", scope="public")

This event will be available for all users.

Possible scope values are: ``public``, ``users``, ``staff``, ``superuser`` (default)

Queries
~~~~~~~

Available queries are:

``publicEvents``, ``usersEvents``, ``staffEvents``, ``allEvents`` (for the superuser)

Example: public events:

 .. highlight:: javascript

::

   {
      publicEvents(first:10) {
         edges {
            node {
               name
               event_class
            }
         }
      }
   }
   

Get all error events (must be logged in as superuser):

::

   {
      allEvents(eventClass_Icontains: "error") {
         edges {
            node {
               name
               eventClass
               request
               notes
            }
         }
      }
   }


Available filters: ``Icontains``, ``Iexact``, ``Istartswith``

Filterable fields: ``name``, ``eventClass``, ``datePosted``
