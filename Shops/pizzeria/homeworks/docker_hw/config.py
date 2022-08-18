import os
from dataclasses import dataclass
from flask import Flask
from peewee import SqliteDatabase


@dataclass
class BaseConfig:
    SERVER_NAME = '127.0.0.1:5000'
    DEBUG = True
    SECRET_KEY = os.environ.get('os_secret_key')
    DB_NAME = 'sqlite.db'


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SqliteDatabase(app.config.get('DB_NAME'))
