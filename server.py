# -*- coding: utf-8 -*-

from flask import render_template

from app import app
from sfec.api.product import register_product_resource
from sfec.api.user import register_user_resource
from sfec.controllers.user import user_api
from sfec.controllers.order import order_api


register_product_resource()
register_user_resource()

app.register_blueprint(user_api)
app.register_blueprint(order_api)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
