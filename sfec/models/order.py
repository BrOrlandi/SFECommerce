# -*- coding: utf-8 -*-

from storm.references import Reference, ReferenceSet
from storm.properties import Int, Unicode

from sfec.models.user import Customer, Vendor
from sfec.models.base import BaseModel


class Order(BaseModel):

    __storm_table__ = "sfec_order"

    status = Unicode()
    customer_service_id = Int()

    customer_service = Reference(customer_service_id,
                                 'CustomerService.order_id')
    products = ReferenceSet('Order.id', 'OrderProduct.order_id')

    def __init__(self):
        self.status = "Buying"


class OrderProduct(BaseModel):

    __storm_table__ = "sfec_order_product"

    quantity = Int()
    order_id = Int()
    product_id = Int()

    order = Reference(order_id, 'Order.id')
    product = Reference(product_id, 'Product.id')

    def __init__(self, product):
        self.product = product


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
