from dataclasses import dataclass
from flask import Flask
from registration_service import Users


@dataclass
class BaseConfig:
    SERVER_NAME = '127.0.0.1:5000'
    DEBUG = True
    SECRET_KEY = 'eu%lwzmzp22^052go0&94k*nm0hik7_8_ewm^h0b6gsc#c71je'
    STORAGE_FILE = 'users.json'


app = Flask(__name__)
app.config.from_object(BaseConfig)

users = Users(app.config.get('STORAGE_FILE'), app.config.get('SECRET_KEY'))
