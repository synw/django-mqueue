.. Django Mqueue documentation master file, created by
   sphinx-quickstart on Tue Mar 29 14:18:50 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Django Mqueue's documentation
=============================

To install: ``pip install django-mqueue``

Add to INSTALLED_APPS: 

.. highlight:: python

::

   "mqueue",

Run the migrations.

.. usage

.. toctree::
	:maxdepth: 2
	:caption: Usage
   
	usage/create_event
	usage/registered_models
	usage/watchers
	usage/retrieve_events
	usage/hooks

.. livefeed

.. toctree::
	:maxdepth: 2
	:caption: Real time events
	
	livefeed/livefeed

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
