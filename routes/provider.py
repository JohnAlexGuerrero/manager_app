from flask import Blueprint
from flask import render_template, redirect, request
from flask import jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model

from models.provider import Provider

provider = Blueprint('providers', __name__)

@provider.route('/providers/new', methods=['GET'])
def new_provider():
    return render_template('provider/new.html')

@provider.route('/api/providers/create', methods=['POST'])
def add_provider():
    json = request.get_json(force=True)

    if json.get('name') is None:
        return jsonify({'message': 'Bad request'}), 400

    
    name, nit, address, city, sellerman, phone, num_mobil = [fm for fm in json.values()]
    
    provider = Provider.create(
        name=name,
        nit=nit,
        address=address,
        city=city,
        sellerman=sellerman,
        phone=phone,
        num_mobil=num_mobil
    )
        
    response = {
        'company': {
                'name':name,
                'nit':nit,
                'address':address,
                'city':city,
                'sellerman':sellerman,
                'phone':phone,
                'num_mobil':num_mobil
            },
        'message': f'El proveedor {name} fue creado con exito'
    }
    
    return jsonify(response)

@provider.route('/api/providers/all')
def all_providers():
    providers = Provider.select()
    items = [model_to_dict(item) for item in providers]
    return items