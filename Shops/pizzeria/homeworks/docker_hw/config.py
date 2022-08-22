import json
from dataclasses import dataclass
from flask import Flask
from peewee import SqliteDatabase


@dataclass
class BaseConfig:
    SERVER_NAME: str
    DEBUG: bool
    SECRET_KEY: str
    DB_NAME: str


with open('config.json') as json_config:
    base_config = BaseConfig(**json.load(json_config))

app = Flask(__name__)
app.config.from_object(base_config)
db = SqliteDatabase(app.config.get('DB_NAME'))
