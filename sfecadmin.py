# -*- coding: utf-8 -*-

import sys

import IPython
from storm.tracer import debug

from sfec.database.runtime import *
from sfec.models.user import *
from app import app


if __name__ == '__main__':
    """Utilidade para realizar testes e verificações na base de dados"""
    store = get_default_store()

    if len(sys.argv) < 2:
        print 'Usage: python sfecadmin.py [OPTIONS]'
        print ''
        print "'OPTIONS' is one of:"
        print ''
        print 'create_user <email> <name>                  New user'
        print 'dbinit                                      Execute the SQL, recreate the schema.'
        print '--sql                                       Show sql commands'
        print '--console                                   Enter console mode'
        print ''


    if '--sql' in sys.argv:
        debug(True, stream=sys.stdout)

    if 'create_user' in sys.argv:
        option_index = sys.argv.index('create_user')

        user = User()
        user.email = unicode(sys.argv[option_index+1])
        user.name = unicode(sys.argv[option_index+2])
        user.set_password(unicode(raw_input('password: ')))
        store.add(user)
        store.commit()

    if 'dbinit' in sys.argv:
        sqlfile = open("./data/sql/schema-00.sql","r")
        schema = sqlfile.read()
        sqlfile.close()

        statements = schema.split(";")

        for stmt in statements:
            store.execute(stmt)
        store.commit()        

        print "DB cleanead and initialized"

    if '--console' in sys.argv:
        IPython.embed()
