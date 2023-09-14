from flask import Blueprint
from flask import render_template, redirect, request

from models.provider import Provider

provider = Blueprint('providers', __name__)

@provider.route('/providers/new', methods=['GET'])
def new_provider():
    return render_template('provider/new.html')

@provider.route('/providers/new', methods=['POST'])
def add_provider():
    name = request.form['name']
    
    provider = Provider.create(name=name)
    return redirect('/shoppings/new')