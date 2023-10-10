from peewee import Model
from peewee import CharField, DateField, IntegerField

from db.database import database

class BaseModel(Model):
    class Meta:
        database=database

class Client(BaseModel):
    name = CharField(max_length=100)
    num_doc = CharField(max_length=10,default='2222222222')
    address = CharField(max_length=100, null=True)
    phone = CharField(max_length=100, null=True)
    

        