Graphql Api
===========

It is possible to query for public events, users events and staff events.

Settings
~~~~~~~~

Install with ``pip install graphene-django django-filter``

 .. highlight:: python

::

   INSTALLED_APPS += ("graphene_django", "django_filters",)

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
   from django.views.decorators.csrf import csrf_exempt
   from graphene_django.views import GraphQLView
   
   urlpatterns = [
    # ...
    path('graphql', GraphQLView.as_view()),
   ]
   
   if settings.DEBUG:
      urlpatterns += [path('graphiql', csrf_exempt(GraphQLView.as_view(graphiql=True)))]

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

Go to ``http://localhost:8000/graphiql/`` to test the queries

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
               eventClass
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
