from flask import Flask
from storage import Storage

storage = Storage("storage.json")
app = Flask(__name__)


secret_key = 'qwerty'


