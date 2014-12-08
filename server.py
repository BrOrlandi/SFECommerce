# -*- coding: utf-8 -*-

from flask import render_template

from app import app
from sfec.api.product import register_product_resource
from sfec.api.user import register_user_resource
from sfec.api.order import register_order_resource
from sfec.controllers.user import user_api
from sfec.controllers.order import order_api


register_product_resource()
register_user_resource()
register_order_resource()

app.register_blueprint(user_api, url_prefix='/api')
app.register_blueprint(order_api, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin',
                         app.config['ALLOWED_DOMAIN'])
    response.headers.add('Access-Control-Max-Age', 0)
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
    return response



if __name__ == '__main__':
    app.run(host='0.0.0.0')
