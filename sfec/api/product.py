# -*- coding: utf-8 -*-

from flask.ext.restful import fields

from app import api
from sfec.api.base import BaseResource
from sfec.api.decorators import FinalResource
from sfec.models.product import Product


@FinalResource
class ProductResource(BaseResource):

    properties = {
        'id': fields.Integer,
        'name': fields.String,
        'stock': fields.Integer,
        'description': fields.String,
        'price': fields.Float,
        'is_available': fields.Boolean,
        'category_list': fields.List(fields.String),
    }

    table = Product

    order_by = Product.name

    filters = {
        'id': Product.id,
        'name': Product.name,
    }


def register_product_resource():
    api.add_resource(ProductResource, '/products', endpoint='products')
