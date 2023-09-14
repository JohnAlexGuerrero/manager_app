from flask import Flask

from routes.inventory import inventory
from routes.home import home
from routes.provider import provider
from routes.shopping import shopping

from db.database import database
from models.inventory import Product
from models.provider import Provider, Invoice, ProductsInvoice

app = Flask(__name__)

# database.create_tables([Provider, Invoice, ProductsInvoice])

app.register_blueprint(inventory)
app.register_blueprint(home)
app.register_blueprint(provider)
app.register_blueprint(shopping)

