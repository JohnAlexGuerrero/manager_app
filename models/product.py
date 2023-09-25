from peewee import Model
from peewee import CharField, DateField
from db.database import database

class BaseModel(Model):
    class Meta:
        database=database

class Product(BaseModel):
    name = CharField(max_length=100, unique=True)
    code = CharField(max_length=10, unique=True)
    unit = CharField(max_length=10, default='und', unique=False)
    createdAt = DateField()
    updatedAt = DateField()