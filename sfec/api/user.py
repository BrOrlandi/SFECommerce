# -*- coding: utf-8 -*-

from flask.ext.restful import fields

from app import api
from sfec.api.base import BaseResource
from sfec.api.decorators import FinalResource
from sfec.api.fields import DateTimeInt
from sfec.models.user import User


@FinalResource
class UsersResource(BaseResource):

    properties = {
        'id': fields.Integer,
        'name': fields.String,
        'email': fields.String,
        'birth_date': DateTimeInt,
        'register_date': DateTimeInt,
    }

    table = User

    order_by = User.name

    filters = {
        'name': User.name,
        'email': User.email,
    }


def register_user_resource():
    api.add_resource(UsersResource, '/users', endpoint='users')
