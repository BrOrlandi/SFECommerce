# -*- coding: utf-8 -*-

from storm.base import Storm
from storm.properties import Unicode, Int, Decimal, Bool
from storm.references import ReferenceSet

from sfec.models.base import BaseModel


class Product(BaseModel):

    __storm_table__ = "sfec_product"

    name = Unicode()

    stock = Int(default=0)

    description = Unicode()

    price = Decimal()

    is_available = Bool(default=False)

    categories = ReferenceSet('Product.id', 'CategoryProduct.product_id',
                              'CategoryProduct.category_id', 'Category.id')


class Category(BaseModel):

    __storm_table__ = "sfec_category"

    name = Unicode()

    products = ReferenceSet('Category.id', 'CategoryProduct.category_id',
                            'CategoryProduct.product_id', 'Product.id')

    def __init__(self, name):
        self.name = name


class CategoryProduct(Storm):

    __storm_table__ = "sfec_category_product"

    __storm_primary__ = "category_id", "product_id"

    category_id = Int()
    product_id = Int()
