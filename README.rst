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
	    uuid = ShortUUIDField()

Enjoy!

Notes
=====

* ShortUUIDField is a subclass of django.db.models.CharField

* You can pass usual Django CharField parameters on init, although some of them are added/overwritten: 
    + max_length=22 (since we are using base-57 format which is fixed at 22 characters)
    + blank=True, editable=False (set auto=False to remove these fields enforcement)

* Uses shortuuid.uuid() that generates uuid4 random values
