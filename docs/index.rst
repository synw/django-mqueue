.. Django Mqueue documentation master file, created by
   sphinx-quickstart on Tue Mar 29 14:18:50 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Django Mqueue's documentation
=============================

To install: ``pip install django-mqueue``, then add ``'mqueue',`` to INSTALLED_APPS. Make migrations
and run them.

.. usage

.. toctree::
	:maxdepth: 2
	:caption: Usage
   
	usage/create_event
	usage/registered_models
	usage/watchers
	usage/retrieve_events
	usage/hooks

.. logs

.. toctree::
	:maxdepth: 2
	:caption: Logs handler
	
	logs/logs_handler

.. settings

.. toctree::
	:maxdepth: 2
	:caption: Settings

	settings/graphical_settings

.. toctree::
	:maxdepth: 2
	:caption: Graphql Api

	api/api




