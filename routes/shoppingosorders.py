from flask import Blueprint
from flask import render_template, redirect, request

from peewee import fn

# from models.provider import Invoice, Provider
# from models.inventory import Product
from models.shopping import ShoppingsOrder

order = Blueprint('order', __name__)

@order.route('/order')
def home():
    sum_total = Shopping.select(fn.Sum(Shopping.value)).scalar()
    shoppings = Shopping.select().order_by(Shopping.createdAt.desc())
    
    return render_template('shopping/index.html', items=shoppings, count_items=len(shoppings), total=sum_total)

@shopping.route('/shoppings/new', methods=['GET'])
def new_invoice():
    providers = Provider.select(Provider.name)
    products = Product.select().dicts()
    items = [item for item in products]
    # print(type(json.dumps(model_to_dict(products))))
    print((items))
    print(type(items))
    
    return render_template('shopping/new.html', providers=providers, items=items)

@shopping.route('/shoppings/new', methods=['POST'])
def add_invoice():
    for rs in request.form:
        print(rs)
    return redirect('/shoppings')