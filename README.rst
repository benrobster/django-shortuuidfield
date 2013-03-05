django-shortuuidfield
----------------

Provides a ShortUUIDField for your Django models which uses the base-57 "Short UUID" package at https://github.com/stochastic-technologies/shortuuid/ .

Originally, a fork from David Cramer's excellent django-uuidfield, but not much is left of that besides a bit of structure.

Installation
============

Install it with pip (or easy_install)::

	pip install django-shortuuidfield

Usage
=====

First you'll need to attach a ShortUUIDField to your class. This acts as a char(22) to maintain compatibility with SQL versions::

	from shortuuidfield import ShortUUIDField
	
	class MyModel(models.Model):
	    uuid = ShortUUIDField(auto=False)

Enjoy!