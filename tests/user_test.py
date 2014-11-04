# -*- coding: utf-8 -*-

from unittest import TestCase

from sfec.database.runtime import get_test_store
from sfec.models.user import Admin, Customer, User, Vendor
from sfec.models.views import AdminView, CustomerView, VendorView

class ModelTest(TestCase):

    def test_create_admin(self):
        store = get_test_store()

        # Create the user
        user = User()
        user.email = u'heisenberg@meth.com'
        user.name = u'Walter White'
        user.set_password('foobar')
        store.add(user)

        # Admin subclass
        admin = Admin()
        admin.user = user
        store.add(admin)

        store.commit()

        # Retrieve the user and validate the results
        test_admin = store.find(AdminView, email=u'heisenberg@meth.com').one()
        self.assertEqual('Walter White', test_admin.name)

    def test_create_customer(self):
        store = get_test_store()

        # Create the user
        user = User()
        user.email = u'walter@meth.com'
        user.name = u'Walter White'
        user.set_password('foobar')
        store.add(user)

        # Admin subclass
        admin = Customer()
        admin.user = user
        store.add(admin)

        store.commit()

        # Retrieve the user and validate the results
        test_admin = store.find(CustomerView, email=u'walter@meth.com').one()
        self.assertEqual('Walter White', test_admin.name)

    def test_create_client(self):
        store = get_test_store()

        # Create the user
        user = User()
        user.email = u'white@meth.com'
        user.name = u'Walter White'
        user.set_password('foobar')
        store.add(user)

        # Admin subclass
        admin = Vendor()
        admin.user = user
        store.add(admin)

        store.commit()

        # Retrieve the user and validate the results
        test_admin = store.find(VendorView, email=u'white@meth.com').one()
        self.assertEqual('Walter White', test_admin.name)
