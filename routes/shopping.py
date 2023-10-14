from flask import Blueprint
from flask import render_template, redirect, request

from peewee import fn

from models.provider import Provider
from models.inventory import Product
from models.shopping import Shopping
from models.inventory import Inventory

shopping = Blueprint('shoppings', __name__)

@shopping.route('/shoppings')
def home():
    sum_total = Shopping.select(fn.Sum(Shopping.value)).scalar()
    shoppings = Shopping.select().order_by(Shopping.createdAt.desc())
    
    return render_template('shopping/index.html', items=shoppings, count_items=len(shoppings), total=sum_total)

@shopping.route('/shoppings/new', methods=['GET'])
def new_invoice():
    providers = Provider.select(Provider.name)
    inventories = Inventory.select()
    items = []
    
    for itm in inventories:
        product = {
            "id":itm.product.code,
            "name": itm.product.name,
            "stock":itm.stock,
            "unit":itm.product.unit,
            "price": itm.price
        }
        
        items.append(product)
    
    return render_template('shopping/new.html', providers=providers, items=items)

@shopping.route('/shoppings/new', methods=['POST'])
def add_invoice():
    for rs in request.form:
        print(rs)
    return redirect('/shoppings')
