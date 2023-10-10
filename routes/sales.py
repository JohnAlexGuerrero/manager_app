from flask import Blueprint, render_template, request, redirect
from playhouse.shortcuts import model_to_dict, dict_to_model
import json

from models.sale import Sale
from models.client import Client


sales = Blueprint('sales', __name__)

@sales.route('/sales')
def home():
    # user_obj = User.select().where(User.username == 'charlie').get()
    # json_data = json.dumps(model_to_dict(user_obj))
    clients = []
    return render_template('sales/index.html', clients=clients)
