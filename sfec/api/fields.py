# -*- coding: utf-8 -*-

from time import mktime

from flask.ext.restful import fields


class DateTimeInt(fields.Raw):
    def format(self, value):
        time = mktime(value.timetuple()) * 1000
        return int(time)
