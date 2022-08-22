from http import HTTPStatus
from flask import request, jsonify
from config import app, db
from registration_service import UsersAuthService
from models import User

users = UsersAuthService(User, app.config.get('SECRET_KEY'))
db.create_tables([User], safe=True)


@app.route('/register', methods=['POST'])
def register_user():
    user_credentials = request.get_json()
    response = None
    http_code = None
    if not users.get_user(user_credentials.get('email')):
        users.create_user(user_credentials)
        response = {"status": "ok"}
        http_code = HTTPStatus.CREATED
    else:
        response = {"status": "error", "detail": "User already exists"}
        http_code = HTTPStatus.BAD_REQUEST
    return jsonify(response), http_code


@app.route('/login', methods=['POST'])
def login():
    user_credentials = request.get_json()
    response = None
    http_code = None
    token = users.check_credentials(user_credentials)
    if token:
        response = {"status": "ok", "token": token}
        http_code = HTTPStatus.OK
    else:
        response = {"status": "error", "detail": "Incorrect email or password"}
        http_code = HTTPStatus.BAD_REQUEST
    return jsonify(response), http_code
