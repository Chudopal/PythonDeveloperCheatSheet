from config import app, users
from flask import request, jsonify


@app.route('/register', methods=['POST'])
def register_user():
    user_credentials = request.get_json()
    response = None
    http_code = None
    if not users.get_user(user_credentials.get('email')):
        users.save_user(user_credentials)
        response = {"status": "ok"}
        http_code = 201
    else:
        response = {"status": "error", "detail": "User already exists"}
        http_code = 400
    return jsonify(response), http_code


@app.route('/login', methods=['POST'])
def login():
    user_credentials = request.get_json()
    response = None
    http_code = None
    token = users.check_credentials(user_credentials)
    if token:
        response = {"status": "ok", "token": token}
        http_code = 200
    else:
        response = {"status": "error", "detail": "Incorrect email or password"}
        http_code = 400
    return jsonify(response), http_code
