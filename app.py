# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.restful import Api

from sfec.config import Config

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app, prefix='/api')
