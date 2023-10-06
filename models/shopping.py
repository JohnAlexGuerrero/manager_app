from peewee import Model
from peewee import ForeignKeyField, CharField, DecimalField, DateField, FloatField
from db.database import database

from models.provider import Provider
from models.product import Product

class BaseModel(Model):
    class Meta:
        database=database

class Shopping(BaseModel):
    provider = ForeignKeyField(Provider, backref='shoppings')
    number = CharField(max_length=10, unique=True)
    createdAt = DateField()
    expirationAt = DateField()
    value = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    way_to_pay = CharField(max_length=10)
    
    
class ShoppingsOrder(BaseModel):
    shopping = ForeignKeyField(Shopping, backref='shoppingsorders')
    product = ForeignKeyField(Product, backref='shoppingsorders')
    quantity = FloatField(default=0.0)
    price = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def save(self):
        self.total = self.price * self.quantity