# -*- coding: utf-8 -*-

from flask.ext.restful import fields

from app import api
from sfec.api.base import BaseResource
from sfec.api.decorators import FinalResource
from sfec.models.order import *
from sfec.api.fields import ProductsField


@FinalResource
class OrderResource(BaseResource):

    properties = {
        'id': fields.Integer,
        'status': fields.String,
        'user_id': fields.Integer,
        'products': ProductsField,
    }

    table = Order

    order_by = Order.id

    filters = {
        'id': Order.id,
        'user_id': Order.user_id,
    }

def register_order_resource():
    api.add_resource(OrderResource, '/orders', endpoint='orders')
