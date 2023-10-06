from peewee import Model
from peewee import ForeignKeyField, DecimalField, CharField, DateField

from models.provider import Provider
from models.shopping import Shopping
from db.database import database

class BaseModel(Model):
    class Meta:
        database=database

class Payment(BaseModel):
    provider = ForeignKeyField(Provider, backref='payments')
    shopping = ForeignKeyField(Shopping, backref='payments')
    description = CharField(max_length=150, null=True)
    value = DecimalField(max_digits=10, decimal_places=2, default=0.0)
    createdAt = DateField()
    