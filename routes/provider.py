from flask import Blueprint
from flask import render_template, redirect, request

from models.provider import Provider

provider = Blueprint('providers', __name__)

@provider.route('/providers/new', methods=['GET'])
def new_provider():
    return render_template('provider/new.html')

@provider.route('/providers/new', methods=['POST'])
def add_provider():
    name, nit, address, city, sellerman, phone, num_mobil = [fm for fm in request.form.values()]
    provider = Provider.create(name=name, nit=nit, city=city, sellerman=sellerman, phone=phone, num_mobil=num_mobil)
    return redirect('/shoppings/new')