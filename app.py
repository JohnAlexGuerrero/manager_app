from flask import Flask
from routes.inventory import inventory
from db.database import database
from models.inventory import Product

app = Flask(__name__)

# database.create_tables([Product])

app.register_blueprint(inventory)

