# -*- coding: utf-8 -*-

from flask.ext.restful import fields

from app import api
from sfec.api.base import BaseResource
from sfec.api.decorators import FinalResource
from sfec.api.fields import DateTimeInt
from sfec.models.user import User
from sfec.models.views import AdminView, VendorView, CustomerView
from sfec.controllers.decorators import require_admin


class BaseUsersResource(BaseResource):

    properties = {
        'id': fields.Integer,
        'name': fields.String,
        'email': fields.String,
        'is_admin': fields.Boolean,
        'birth_date': DateTimeInt,
        'register_date': DateTimeInt,
    }

    @require_admin
    def get(self, id=None):
        return super(BaseUsersResource,self).get(id=id)


@FinalResource
class UsersResource(BaseUsersResource):

    table = User

    order_by = User.name

    filters = {
        'id': User.id,
        'name': User.name,
        'email': User.email,
    }


@FinalResource
class AdminsResource(BaseUsersResource):

    table = AdminView

    order_by = AdminView.name

    filters = {
        'id': AdminView.id,
        'name': AdminView.name,
        'email': AdminView.email,
    }


@FinalResource
class VendorsResource(BaseUsersResource):

    table = VendorView

    order_by = VendorView.name

    filters = {
        'id': VendorView.id,
        'name': VendorView.name,
        'email': VendorView.email,
    }


@FinalResource
class CustomersResource(BaseUsersResource):

    table = CustomerView

    order_by = CustomerView.name

    filters = {
        'id': CustomerView.id,
        'name': CustomerView.name,
        'email': CustomerView.email,
    }


def register_user_resource():
    api.add_resource(UsersResource, '/users', endpoint='users')
    api.add_resource(AdminsResource, '/admins', endpoint='admins')
    api.add_resource(VendorsResource, '/vendors', endpoint='vendors')
    api.add_resource(CustomersResource, '/customers', endpoint='customers')
