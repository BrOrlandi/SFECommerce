# -*- coding: utf-8 -*-

import re
from flask import Blueprint, g, session, request, abort

from sfec.models.user import *
from sfec.models.views import *
from sfec.database.runtime import get_default_store
from sfec.controllers.decorators import *

user_api = Blueprint('user_api', __name__)

def is_email_address_valid(email):
    """Validate the email address using a regex."""
    if not re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
        return False
    return True

@user_api.route("/register", methods=['POST'])
def register():
	"""Register a new user."""
	if not is_email_address_valid(request.form['email']):
		return "E-mail not valid!"

	store = get_default_store()
	# Default user is customer, an admin must change the user to staff member (admin or vendor)
	found = store.find(User, User.email == request.form['email']).one()
	if found is not None:
		return "E-mail already taken!"
	new_customer = Customer()
	user = User()
	user.name = request.form['name']
	user.email = request.form['email']
	user.set_password(request.form['password'])
	user.birth_date = datetime.strptime(request.form['birth_date'],"%m-%d-%Y")
	store = get_default_store()
	new_customer.user = user
	store.add(new_customer)
	store.commit()
	return "Success!"



@user_api.route('/login', methods=['POST'])
def login():
	"""Log the user in."""
	store = get_default_store()
	user = User.authenticate(store, request.form['email'],request.form['password'])
	if user:
		session['user'] = user.id
		return "True"
	return "False"

@user_api.route('/logout', methods=['GET'])
@require_login
def logout():
	session.pop('user',None)
	return "True"

@user_api.route('/users/<int:user_id>/set_vendor', methods=['GET'])
@require_admin
def set_vendor(user_id):
	store = get_default_store()
	user = store.find(User, User.id == user_id).one()
	if user is None:
		abort(404)
	user = store.find(VendorView, VendorView.id == user_id).one()
	if user is not None:
		return "Already Vendor!"
	vendor = Vendor()
	vendor.user = user
	store.add(vendor)
	return "True"

@user_api.route('/users/<int:user_id>/set_admin', methods=['GET'])
@require_admin
def set_admin(user_id):
	store = get_default_store()
	user = store.find(User, User.id == user_id).one()
	if user is None:
		abort(404)
	user = store.find(AdminView, AdminView.id == user_id).one()
	if user is not None:
		return "Already Admin!"
	admin = Admin()
	admin.user = user
	store.add(admin)
	return "True"
