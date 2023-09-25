from flask import Blueprint, render_template, request, redirect
from models.product import Product
from models.inventory import Inventory

from datetime import datetime

product = Blueprint('products', __name__)

@product.route('/products')
def index():
    return render_template('product/index.html')

@product.route('/products/add-product', methods=['GET'])
def new_form():
    return render_template('product/new.html')

@product.route('/products/new', methods=['POST'])
def new():
    name, code, stock, unit, cost, price = [field for field in request.form.values()]
    product = Product.create(name=name, code=code, unit=unit, createdAt=datetime.now(),updatedAt=datetime.now())
    inventory_item = Inventory.create(product_id=product.id,stock=stock, cost=cost, price=price, createdAt=datetime.now(),updatedAt=datetime.now())
    return redirect('/inventory')