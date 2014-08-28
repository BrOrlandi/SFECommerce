# -*- coding: utf-8 -*-

from datetime import datetime
from cgi import escape
import json
from time import mktime

from storm.base import Storm
from storm.properties import Int, Property, Unicode
from storm.store import AutoReload


class BaseModel(Storm):
    """Provides utilities for most of the SFEC database models"""

    __storm_primary__ = 'id'

    id = Int(default=AutoReload)

    #
    # Static API
    #

    @classmethod
    def find(cls, store, id):
        return store.find(cls, id=id).one()

    @classmethod
    def exists(cls, store, id):
        relation = cls.find(store, id)
        return relation is not None

    #
    # Public API
    #

    def dict(self):
        """Returns this object as a dictionary"""
        dictionary = {}
        for key, value in self.__class__.__dict__.iteritems():
            if isinstance(value, Property):
                dictionary[key] = getattr(self, key)
        return dictionary

    def json(self):
        """Returns this object in JSON"""
        dictionary = {}
        for key, value in self.dict().iteritems():
            dictionary[key] = value
            if isinstance(value, datetime):
                # Transforms the datetime into a JSON representation
                dictionary[key] = mktime(value.timetuple()) * 1000
        return json.dumps(dictionary)

    #
    # Hooks
    #

    def __storm_pre_flush__(self):
        """Escape any string into a html escaped string"""
        attributes = self.__class__.__dict__.iteritems()
        attributes = {key: value for key, value in attributes
                      if type(value) == Unicode}

        for key, value in attributes.iteritems():
            value = getattr(self, key) or u''
            setattr(self, key, escape(value))
