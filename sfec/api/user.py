# -*- coding: utf-8 -*-

from flask.ext.restful import fields

from app import api
from sfec.api.base import BaseResource
from sfec.api.decorators import FinalResource
from sfec.api.fields import DateTimeInt
from sfec.models.user import User
from sfec.models.views import AdminView, VendorView, CustomerView


class BaseUsersResource(BaseResource):

    properties = {
        'id': fields.Integer,
        'name': fields.String,
        'email': fields.String,
        'birth_date': DateTimeInt,
        'register_date': DateTimeInt,
    }

    order_by = User.name

    filters = {
        'name': User.name,
        'email': User.email,
    }


@FinalResource
class UsersResource(BaseUsersResource):

    table = User


@FinalResource
class AdminsResource(BaseUsersResource):

    table = AdminView


@FinalResource
class VendorsResource(BaseUsersResource):

    table = VendorView


@FinalResource
class CustomersResource(BaseUsersResource):

    table = CustomerView


def register_user_resource():
    api.add_resource(UsersResource, '/users', endpoint='users')
    api.add_resource(AdminsResource, '/admins', endpoint='admins')
    api.add_resource(VendorsResource, '/vendors', endpoint='vendors')
    api.add_resource(CustomersResource, '/customers', endpoint='customers')
