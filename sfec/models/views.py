# -*- coding: utf-8 -*-

from sfec.models.user import User


class AdminView(User):

    __storm_table__ = "sfec_admin_view"


class VendorView(User):

    __storm_table__ = "sfec_vendor_view"


class CustomerView(User):

    __storm_table__ = "sfec_customer_view"
