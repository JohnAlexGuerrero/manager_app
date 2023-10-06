from flask import Blueprint, render_template, request, redirect
from models.inventory import Inventory
from models.product import Product

inventory = Blueprint('inventory', __name__)

@inventory.route('/inventory')
def home():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 10
    
    products = Inventory.select()
    items = products.paginate(page, items_per_page)
    print()
    return render_template('inventory/index.html', num_items=len(items), items=items, num_pagination=round(len(products)/10))

@inventory.route('/inventory/new', methods=['GET'])
def form_product():
    return render_template('inventory/new.html')

@inventory.route('/inventory/new', methods=['POST'])
def new_product():
    name, code, stock, unit, cost, price = [field for field in request.form.values()]
    
    product = Product.create(name=name, code=code, stock=stock, unit=unit, cost=cost, price=price)
    return redirect('/inventory')