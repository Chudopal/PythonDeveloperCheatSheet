from flask import jsonify, request
from models import User
from config import app, db, answer_by_code
import hashlib
import jwt


def credentials_ctrl(): 
    if not request.form.get('Email') or not request.form.get('Password'):
        return answer_by_code.get("Credential")


def get_md5_password(password):    
    md5_hash = hashlib.md5()
    md5_hash.update(bytes(password, 'utf-8'))
    return md5_hash.hexdigest()


def check_user_data_for_reg():
    email = request.form.get('Email')
    password = request.form.get('Password')
    
    if not User.query.get(email):
        password = get_md5_password(password)

        db.session.add(
            User(email=email, password=password)
        )
        db.session.commit()

        answer = answer_by_code.get(201)

    else:
        answer = answer_by_code.get(400).get("already_exists")

    return answer


def check_user_data_for_auth():
    email = request.form.get('Email')
    password = get_md5_password(request.form.get('Password'))

    user = User.query.get(email)

    if not user:
        answer = answer_by_code.get(400).get("User_doesn't_exist")

    elif user.password == password:   
        answer = answer_by_code.get(200)
        answer.update({"token": jwt.encode({"some": "payload"}, email, algorithm="HS256")})

    else:
        answer = answer_by_code.get(400).get("Passwords_ctrl")

    return answer


@app.route('/reg', methods=['POST'])
def user_registration():
    result = credentials_ctrl()
    if not result:
        result = check_user_data_for_reg() 
    
    return jsonify(result)


@app.route('/auth', methods=['POST'])
def user_authentication():
    result = credentials_ctrl()
    if not result:
        result = check_user_data_for_auth() 
    
    return jsonify(result)
