from peewee import Model, CharField
from config import db


class User(Model):
    class Meta:
        database = db

    uuid = CharField(primary_key=True)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
