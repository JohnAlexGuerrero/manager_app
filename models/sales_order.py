from peewee import Model
from peewee import FloatField, CharField, ForeignKeyField

from models.sale import Sale
from models.product import Product

from db.database import database

class BaseModel(Model):
    class Meta:
        database=database

class SalesOrder(BaseModel):
    sales = ForeignKeyField(Sale, backref='salesorders')
    product = ForeignKeyField(Product, backref='salesorders')       