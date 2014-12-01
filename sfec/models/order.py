# -*- coding: utf-8 -*-

from storm.references import Reference, ReferenceSet
from storm.properties import Int, Unicode

from sfec.models.user import User, Customer, Vendor
from sfec.models.base import BaseModel


class Order(BaseModel):

    __storm_table__ = "sfec_order"

    status = Unicode()

    products = ReferenceSet('Order.id', 'OrderProduct.order_id')

    user_id = Int()
    user = Reference(user_id, User.id)

    def __init__(self):
        self.status = u"Buying"

class OrderProduct(BaseModel):

    __storm_table__ = "sfec_order_product"

    quantity = Int()
    order_id = Int()
    product_id = Int()

    order = Reference(order_id, 'Order.id')
    product = Reference(product_id, 'Product.id')

    def __init__(self, order, product, quantity):
        self.order = order
        self.product = product
        self.quantity = quantity

class Cart(BaseModel):

    __storm_table__ = "sfec_cart"

    order_id = Int()
    order = Reference(order_id, 'Order.id')

    user_id = Int()
    user = Reference(user_id, User.id)

    def __init__(self, user):
        self.order = Order()
        self.order.user_id = user.id
        self.user_id = user.id




class CustomerService(BaseModel):

    __storm_table__ = "sfec_customer_service"

    order_id = Int()
    customer_id = Int()
    vendor_id = Int()

    customer = Reference(customer_id, Customer.id)
    vendor = Reference(vendor_id, Vendor.id)
    order = Reference(order_id, Order.id)

    def __init__(self, order, customer, vendor):
        self.order_id = order.id
        self.customer_id = customer.id
        self.vendor_id = vendor.id
