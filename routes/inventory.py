from flask import Blueprint, render_template, request, redirect
from models.inventory import Inventory
from models.product import Product

inventory = Blueprint('inventory', __name__)

@inventory.route('/inventory')
def home():
    products = Inventory.select()
    print(products)
    return render_template('inventory/index.html', num_items=len(products), items=products)

@inventory.route('/inventory/new', methods=['GET'])
def form_product():
    return render_template('inventory/new.html')

@inventory.route('/inventory/new', methods=['POST'])
def new_product():
    name, code, stock, unit, cost, price = [field for field in request.form.values()]
    
    product = Product.create(name=name, code=code, stock=stock, unit=unit, cost=cost, price=price)
    return redirect('/inventory')