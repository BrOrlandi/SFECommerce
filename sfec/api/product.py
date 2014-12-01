# -*- coding: utf-8 -*-

from flask.ext.restful import fields

from app import api
from sfec.api.base import BaseResource
from sfec.api.decorators import FinalResource
from sfec.models.product import Product, Category
from flask.ext.restful import reqparse
from sfec.database.runtime import get_default_store
from sfec.controllers.decorators import require_vendor


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
"""
    @require_vendor
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=unicode, required=True)
        parser.add_argument('stock', type=int, required=True)
        parser.add_argument('description', type=unicode, required=True)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('is_available', type=bool, required=True)
        args = parser.parse_args()
        c = Category(args['name'])
        store = get_default_store()
        store.add(c)
        store.commit()
        return "Success",201

    @require_vendor
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True)
        args = parser.parse_args()
        store = get_default_store()
        c = store.find(Category, Category.id == args['id']).one()
        if c is None:
            return "Fail",404
        store.remove(c)
        store.commit()
        return "Success",204

    @require_vendor
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True)
        parser.add_argument('name', type=unicode, required=True)
        args = parser.parse_args()
        store = get_default_store()
        c = store.find(Category, Category.id == args['id']).one()
        if c is None:
            return "Fail",404
        c.name = args['name']
        store.flush()
        return "Success",201
"""
@FinalResource
class CategoryResource(BaseResource):

    properties = {
        'id': fields.Integer,
        'name': fields.String
    }

    table = Category

    order_by = Category.name

    filters = {
        'id': fields.Integer,
        'name': Category.name,
    }

    @require_vendor
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=unicode, required=True)
        args = parser.parse_args()
        c = Category(args['name'])
        store = get_default_store()
        store.add(c)
        store.commit()
        return "Success",201

    @require_vendor
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True)
        args = parser.parse_args()
        store = get_default_store()
        c = store.find(Category, Category.id == args['id']).one()
        if c is None:
            return "Fail",404
        store.remove(c)
        store.commit()
        return "Success",204

    @require_vendor
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True)
        parser.add_argument('name', type=unicode, required=True)
        args = parser.parse_args()
        store = get_default_store()
        c = store.find(Category, Category.id == args['id']).one()
        if c is None:
            return "Fail",404
        c.name = args['name']
        store.flush()
        return "Success",201




def register_product_resource():
    api.add_resource(ProductResource, '/products', endpoint='products')
    api.add_resource(CategoryResource, '/categories', endpoint='categories')
