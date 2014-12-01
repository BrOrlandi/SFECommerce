# -*- coding: utf-8 -*-

import re
from flask import Blueprint, g, session, request, abort, Response

import json

from sfec.models.order import *
from sfec.models.product import Product
from sfec.database.runtime import get_default_store
from sfec.controllers.decorators import *
from time import mktime

order_api = Blueprint('order_api', __name__)

def create_user_cart():
	user = store.find(User, User.id == session['user']).one()
	# create new cart
	cart = Cart(user)
	store.add(cart)
	store.commit()
	return cart

def get_order_products(order):
	store = get_default_store()
	prods = store.find(OrderProduct, OrderProduct.order_id == order.id)
	order_products = []
	for p in prods:
		pdict = p.product.dict()
		pdict['price'] = float(pdict['price']) # price is decimal
		op = {'product': pdict, 'quantity': p.quantity}
		order_products.append(op)
	return order_products

@order_api.route("/cart", methods=['GET'])
@require_login
def cart():
	""" Get customer cart """
	store = get_default_store()

	cart = store.find(Cart, Cart.user_id == session['user']).one()
	if cart is None:
		cart = create_user_cart()

	orderd = cart.order.dict()
	prods = get_order_products(cart.order)
	orderd['products'] = prods
	json_str = json.dumps(orderd)
	return Response(json_str, mimetype='application/json')

@order_api.route("/cart/add_product", methods=['POST'])
@require_login
def add_product():
	""" Add product to cart """
	store = get_default_store()

	cart = store.find(Cart, Cart.user_id == session['user']).one()
	if cart is None:
		cart = create_user_cart()
	order = cart.order
	product = store.find(Product, Product.id == int(request.form['id'])).one()
	quantity = int(request.form['quantity'])
	op = OrderProduct(order,product,quantity)
	store.add(op)
	store.commit()
	return "Success"

