# -*- coding: utf-8 -*-

from storm.database import create_database
from storm.store import Store
from storm.uri import URI

from app import app


class DatabaseSettings(object):

    def __init__(self, db_file):
        # Registering connection data
        self.db_file = db_file

        # Generating URI to connect to the SQLite database file
        self.uri_string = "sqlite:%s" % (db_file)

    def get_store(self):
        """Generate a instance of the Store object"""
        return Store(create_database(self.uri_string))


config = app.config

default_settings = DatabaseSettings(config['DB_FILE'])
