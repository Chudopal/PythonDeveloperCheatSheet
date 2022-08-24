import hashlib
from config import storage, secret_key
import jwt


def hash_md5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()


def registrate(account):
    account['password'] = hash_md5(account.get('password'))
    email = account.get("email")
    db = storage.get_by_email(email)
    saved_email = db.get(email)
    if email != saved_email:
        return storage.add(account)


def login(account):
    email = account.get("email")
    data = storage.get_by_email(email)
    password = hash_md5(account.get("password"))
    saved_password = data.get("password")
    saved_email = data.get("email")
    if password == saved_password and email == saved_email:
        return make_jwt(data)


def make_jwt(data):
    return jwt.encode(data, secret_key, algorithm='HS256')
