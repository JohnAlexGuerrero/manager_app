from flask import Blueprint
from flask import render_template

shopping = Blueprint('shoppings', __name__)

@shopping.route('/shoppings')
def home():
    return render_template('shopping/index.html')