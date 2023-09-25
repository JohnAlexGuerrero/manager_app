from peewee import Model
from peewee import ForeignKeyField, CharField, DecimalField, DateField
from db.database import database

from models.provider import Provider

class BaseModel(Model):
    class Meta:
        database=database

class Shopping(BaseModel):
    provider = ForeignKeyField(Provider, backref='shoppings')
    number = CharField(max_length=10, unique=True)
    createdAt = DateField()
    expirationAt = DateField()
    value = DecimalField(max_digits=10, decimal_places=2)
    way_to_pay = CharField(max_length=10)