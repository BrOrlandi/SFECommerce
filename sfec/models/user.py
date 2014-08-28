# -*- coding: utf-8 -*-

from datetime import datetime
from hashlib import sha512

from flask import request
from storm.expr import And
from storm.properties import Date, Unicode

from sfec.models.base import BaseModel


class User(BaseModel):

    __storm_table__ = "sfec_user"

    name = Unicode()

    # Basic login data
    email = Unicode()
    password = Unicode()

    birth_date = Date()
    register_date = Date()

    # TODO Missing type attribute

    def __init__(self):
        self.register_date = datetime.now()

    #
    # Static API
    #

    @staticmethod
    def hash(password):
        """The hash function to be used by the table"""
        return unicode(sha512(password).hexdigest())

    @classmethod
    def authenticate(cls, store, email, password):
        """Returns the user that matches the email password combination"""
        pw_hash = cls.hash(password)
        queries = [cls.email == email, cls.password == pw_hash]

        user = store.find(cls, And(*queries)).one()
        if user:
            user.last_login = datetime.now()
            user.last_ip = unicode(request.remote_addr)
            store.commit()
            return user

        return False

    #
    # Public API
    #

    def set_password(self, password):
        self.password = self.hash(password)
