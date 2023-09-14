from flask import Blueprint
from flask import render_template, redirect, request

from models.provider import Invoice, Provider
from models.inventory import Product

shopping = Blueprint('shoppings', __name__)

@shopping.route('/shoppings')
def home():
    list_obj = Provider.select()
     
    return render_template('shopping/index.html', list_obj=list_obj, num_items=len(list_obj))

@shopping.route('/shoppings/new', methods=['GET'])
def new_invoice():
    providers = Provider.select(Provider.name)
    products = Product.select()
    
    return render_template('shopping/new.html', providers=providers, items=products)

@shopping.route('/shoppings/new', methods=['POST'])
def add_invoice():
    for rs in request.form:
        print(rs)
    return redirect('/shoppings')