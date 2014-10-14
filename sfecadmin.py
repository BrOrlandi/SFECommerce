# -*- coding: utf-8 -*-

import random
import sys

import IPython
from storm.tracer import debug

from sfec.database.runtime import *
from sfec.models.user import *
from sfec.models.views import *

from sfec.models.category import *
from sfec.models.product import *
from decimal import Decimal

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
        print 'create_admin <email> <name>                 New admin'
        print 'create_vendor <email> <name>                New vendor/salesperson'
        print 'create_customer <email> <name>              New customer'
        print 'dbinit                                      Execute the SQL, recreate the schema.'
        print 'dbexample                                   Fill database with examples.'
        print '--sql                                       Show sql commands'
        print '--console                                   Enter console mode'
        print ''


    if '--sql' in sys.argv:
        debug(True, stream=sys.stdout)

    user_cmd = ['create_user', 'create_admin', 'create_vendor', 'create_customer']
    user_create = [c for c in user_cmd if c in sys.argv]
    if user_create:
        option_index = sys.argv.index(user_create[0])

        user = User()
        user.email = unicode(sys.argv[option_index+1])
        user.name = unicode(sys.argv[option_index+2])
        user.set_password(unicode(raw_input('password: ')))
        store.add(user)
        store.commit()

    if 'create_admin' in sys.argv:
        admin = Admin()
        admin.user = user
        store.add(admin)
        store.commit()

    if 'create_vendor' in sys.argv:
        vendor = Vendor()
        vendor.user = user
        store.add(vendor)
        store.commit()

    if 'create_customer' in sys.argv:
        customer = Customer()
        customer.user = user
        store.add(customer)
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

    if 'dbexample' in sys.argv:
        user_types = [Admin, Vendor, Customer]
        with open('data/samples/names.txt') as names_file:
            names = names_file.read().split('\n')
        with open('data/samples/surnames.txt') as surnames_file:
            surnames = surnames_file.read().split('\n')
        with open('data/samples/domains.txt') as domains_file:
            domains = domains_file.read().split('\n')

        for i in xrange(25):
            # Generate example data
            full_name = random.choice(names) + ' ' + random.choice(surnames)
            lower_name = full_name.lower()
            email = lower_name.replace(' ', '.') + '@' + random.choice(domains)

            # Apply data on database
            user = User()
            user.email = unicode(email)
            user.name = unicode(full_name)
            user.set_password(unicode('foobar'))
            store.add(user)

            user_type = random.choice(user_types)
            user_cls = user_type()
            user_cls.user = user
            store.add(user_cls)


        # categories

        c1 = Category(u"Hardware")

        with open('data/samples/categories.txt') as categories_file:
            categories = categories_file.read().split('\n')
        with open('data/samples/products.txt') as products_file:
            products = products_file.read().split('\n\n')

        clength = len(categories)
        for i in xrange(clength):
            c = Category(unicode(categories[i]))
            pc = products[i].split("\n")
            for j in xrange(len(pc)):
                data = pc[j].split(",")

                p = Product()
                p.name = unicode(data[0])
                p.stock = int(data[1])
                p.description = unicode(data[2])
                p.price = Decimal(float(data[3]))
                p.is_available = bool(data[4])
                p.categories.add(c)
                p.categories.add(c1)
                store.add(p)

        store.commit()

        print "DB filled with examples"

    if '--console' in sys.argv:
        IPython.embed()
