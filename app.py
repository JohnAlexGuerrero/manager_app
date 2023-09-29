from flask import Flask

from routes.inventory import inventory
from routes.home import home
from routes.provider import provider
from routes.shopping import shopping
from routes.product import product

from db.database import database
from models.inventory import Inventory#, Category, ProductCategory
from models.product import Product#, Category, ProductCategory
from models.provider import Provider
from models.client import Client
from models.shopping import Shopping, ShoppingsOrder

app = Flask(__name__)

database.create_tables([
    Product, Inventory, #Category, ProductCategory
    Provider,
    # Client,
    Shopping, ShoppingsOrder
    ])

app.register_blueprint(inventory)
app.register_blueprint(product)
app.register_blueprint(home)
app.register_blueprint(provider)
app.register_blueprint(shopping)
# app.register_blueprint(ShoppingsOrder)

