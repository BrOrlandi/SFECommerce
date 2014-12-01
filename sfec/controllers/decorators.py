# -*- coding: utf-8 -*-

from flask import session, abort
from functools import wraps
from sfec.database.runtime import get_default_store
from sfec.models.user import *

def require_login(function):

	@wraps(function)
	def wrapper(*args, **kwargs):
		user_id = session.get('user', None)
		if user_id is None:
			abort(403)
		return function(*args, **kwargs)        
	return wrapper

def require_vendor(function):

	@wraps(function)
	def wrapper(*args, **kwargs):
		user_id = session.get('user', None)
		if user_id is None:
			abort(403)
		store = get_default_store()
		vendor = store.find(Vendor, Vendor.id == user_id).one()
		if vendor is None:
			# try as admin
			admin = store.find(Admin, Admin.id == user_id).one()
			if admin is None:
				abort(403)
			
		return function(*args, **kwargs)        
	return wrapper

def require_admin(function):

	@wraps(function)
	def wrapper(*args, **kwargs):
		user_id = session.get('user', None)
		if user_id is None:
			abort(403)
		store = get_default_store()
		admin = store.find(Admin, Admin.id == user_id).one()
		if admin is None:
			abort(403)
			
		return function(*args, **kwargs)        
	return wrapper
