from db.database import database
from peewee import Model
from peewee import CharField, IntegerField, DecimalField

class BaseModel(Model):
    class Meta:
        database=database

class Product(BaseModel):
    name = CharField(max_length=100, unique=True)
    code = CharField(max_length=10, unique=True)
    stock = IntegerField(default=0)
    unit = CharField(max_length=10, default='und', unique=False)
    cost = DecimalField(max_digits=10 ,decimal_places=2, default=0.0)

