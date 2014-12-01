# -*- coding: utf-8 -*-

from time import mktime

from flask.ext.restful import fields


class DateTimeInt(fields.Raw):
    def format(self, value):
        time = mktime(value.timetuple()) * 1000
        return int(time)

class ProductsField(fields.Raw):
    def format(self, value):
    	pf = []
    	for p in value:
    		pd = p.dict()
    		pd['product'] = p.product.dict()
    		del pd['product_id']
    		pf.append(pd)
    	return pf