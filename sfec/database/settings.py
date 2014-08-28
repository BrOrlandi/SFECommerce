# -*- coding: utf-8 -*-

from storm.database import create_database
from storm.store import Store
from storm.uri import URI

from app import app


class DatabaseSettings(object):

    def __init__(self, dbms, username, password, address, db_name):
        # Registering connection data
        self.dbms = dbms
        self.username = username
        self.password = password
        self.address = address
        self.db_name = db_name

        # Generating URI to connect to the RDBMS
        # Exemplo: mysql://username:password@hostname/database_name
        authority = "%s:%s@%s" % (username, password, address)
        uri_string = "%s://%s/%s" % (dbms, authority, db_name)

        self.uri = URI(uri_string)
        self.uri.options['isolation'] = 'read-committed'

    def get_store(self):
        """Generate a instance of the Store object"""
        return Store(create_database(self.uri))


config = app.config

default_settings = DatabaseSettings(config['RDBMS'], config['DB_USER'],
                                    config['DB_PASS'], config['DB_HOST'],
                                    config['DB_NAME'])
