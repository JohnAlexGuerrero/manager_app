from db.database import database
from peewee import Model
from peewee import CharField, DecimalField, DateTimeField, ForeignKeyField, IntegerField, DateField

from models.inventory import Product

class BaseModel(Model):
    class Meta:
        database = database

class Provider(BaseModel):
    name = CharField(max_length=100, unique=True)
    

class Invoice(BaseModel):
    provider = ForeignKeyField(Provider, backref='invoices')
    number = CharField(max_length=10, unique=True)
    createdAt = DateTimeField()
    expirationAt = DateTimeField()
    value = DecimalField(decimal_places=2, max_digits=10, default=0)
    
class ProductsInvoice(BaseModel):
    invoice = ForeignKeyField(Invoice, backref='product_invoice')
    product = ForeignKeyField(Product, backref='product_invoice')
    quantity = IntegerField(default=0)
    price = DecimalField(max_digits=10, decimal_places=2, default=0)
    createdAt = DateField()
    