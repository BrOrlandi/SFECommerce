# -*- coding: utf-8 -*-

from flask import render_template

from app import app
from sfec.api.product import register_product_resource
from sfec.api.user import register_user_resource


register_product_resource()
register_user_resource()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
