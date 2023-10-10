from flask import Blueprint, redirect, render_template, request
from models.client import Client
from flask import jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model

client = Blueprint('clients', __name__)

@client.route('/clients')
def home():
    return render_template('client/index.html')

@client.route('/clients/new', methods=['POST'])
def new_client():
    name, num_doc, address, phone = [field for field in request.form.values()]
    client = Client.create(name=name, num_doc=num_doc, address=address, phone=phone)
    return redirect('/sales')

@client.route('/clients/edit')
def edit_client():
    return ''

@client.route('/api/clients/all', methods=['GET'])
def all():
#        items = HomeCarousel.select()
#    items = [model_to_dict(item) for item in items]
#    return items
    clients = Client.select()
    items = [model_to_dict(item) for item in clients]
    
    return items