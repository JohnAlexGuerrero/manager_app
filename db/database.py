from peewee import MySQLDatabase
from db.variables import NAME_DATABASE, USER, PASSWORD

database = MySQLDatabase(NAME_DATABASE, user=USER, password=PASSWORD)

database.connect()


