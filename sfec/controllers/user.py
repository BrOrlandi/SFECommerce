# -*- coding: utf-8 -*-

from flask import Blueprint, g, session, request

from sfec.models.user import *
from sfec.database.runtime import get_default_store

user_api = Blueprint('user_api', __name__)

@user_api.route('/login', methods=['POST'])
def login():
	"""Log the user in."""
	store = get_default_store()
	user = User.authenticate(store, request.form['usermail'],request.form['password'])
	if user:
		session['user'] = user.id
		return "True"
	return "False"

@user_api.route('/logout', methods=['GET'])
def logout():
	session.pop('user',None)
	return "True"