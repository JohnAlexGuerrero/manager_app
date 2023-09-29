from db.database import database
from peewee import Model
from peewee import CharField, DecimalField, DateTimeField, ForeignKeyField, IntegerField, DateField

class BaseModel(Model):
    class Meta:
        database = database

class Provider(BaseModel):
    name = CharField(max_length=100, unique=True)
    nit = CharField(max_length=15, unique=True)
    address = CharField(max_length=50)
    city = CharField(max_length=50)
    sellerman = CharField(max_length=50)
    phone = CharField(max_length=11, null=True, default='888-8888-888')
    num_mobil = CharField(max_length=11, null=True, default='888-8888-888')
    
    


    