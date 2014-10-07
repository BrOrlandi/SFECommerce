# -*- coding: utf-8 -*-

from flask import abort
from flask.ext.restful import marshal
from storm.store import ResultSet


def FinalResource(cls):
    cls_get = cls.get

    def decorated_get(self, *args, **kwargs):
        data = cls_get(self, *args, **kwargs)

        if isinstance(data, int):
            return data

        if data is None:
            abort(404)

        if isinstance(data, ResultSet):
            data = list(data)
        return marshal(data, self.properties)

    cls.get = decorated_get
    return cls
