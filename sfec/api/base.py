# -*- coding: utf-8 -*-

from flask import request
from flask.ext.restful import Resource
from storm.properties import Unicode, Int
from storm.expr import And, Like

from sfec.database.runtime import get_default_store


class BaseResource(Resource):
    method_decorators = []

    # Properties that will be served by the API
    properties = {}

    # Table or view that will be used for the resource
    table = None

    # Order of the resources to be served
    order_by = None

    # Limit of elements that will be served
    limit = None

    # Filters that may be used for the resource
    filters = {}

    def query(self, column, value):
        """Returns the query for each column type"""
        cls = column.cls
        for column_cls in cls.__mro__:
            column_type = type(column_cls.__dict__.get(column.name))
            if column_type is Unicode:
                return Like(column, '%%%s%%' % value, case_sensitive=False)
            if column_type is Int:
                return column == int(value)
        raise

    def request_filters(self):
        """Returns the general query to be made"""
        query = []
        for key, value in request.args.iteritems():
            column = self.filters.get(key, None)

            if column is None:
                continue

            query.append(self.query(column, value))

        if query:
            query = And(*query)
        return query

    def is_count(self):
        return request.args.get('c', None) is not None

    def get(self, id=None):
        """Serves data via the GET method"""
        store = get_default_store()

        if id is not None:
            id = int(id)
            data = self.table.find(store, id)
            return data

        data = store.find(self.table)

        filters = self.request_filters()
        if filters:
            data = data.find(filters)
        if self.order_by:
            data = data.order_by(self.order_by)
        if self.limit:
            data = data.order_by(self.limit)
        if self.is_count():
            return data.count()

        return data
