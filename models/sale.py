from peewee import Model
from peewee import ForeignKeyField, CharField, DecimalField, DateField
from models.client import Client
 
from db.database import database

class BaseModel(Model):
    class Meta:
        database=database

class Sale(BaseModel):
    client = ForeignKeyField(Client, backref='sales')
    number = CharField(max_length=20, unique=True)
    createdAt = DateField()
    value = DecimalField(max_digits=10, decimal_places=2, defult=0.0)