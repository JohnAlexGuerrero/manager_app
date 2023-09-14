from flask import Blueprint
from flask import render_template, redirect, request

from models.provider import Provider

provider = Blueprint('providers', __name__)

@provider.route('/providers/new', methods=['GET'])
def new_provider():
    return render_template('shopping/new.html')

@provider.route('/providers/new', methods=['POST'])
def add_provider():
    name = [field for field in request.form.values()]
    
    provider = Provider.create(name=name)
    return redirect('/shopping')