from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import hashlib
import jwt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(120), nullable=False)


def get_md5_password(password):    
    md5_hash = hashlib.md5()
    md5_hash.update(bytes(password, 'utf-8'))
    return md5_hash.hexdigest()


def check_user_data_for_reg():
# Добавить контоль данных!!!
    email = request.form.get('Email')
    password = request.form.get('Password')
    
    if not User.query.get(email):
        password = get_md5_password(password)

        db.session.add(
            User(email=email, password=password)
        )
        db.session.commit()

        answer = {"status": "ok"}

    else:
        answer = {
            "status": "error",
            "detail": "User already exists."
        }

    return answer


def check_user_data_for_auth():
    email = request.form.get('Email')
    password = get_md5_password(
        request.form.get('Password')
    )

    user = User.query.get(email)

    if user.password == password:
        answer = {
            "status": "ok",
            "token": jwt.encode({"some": "payload"}, email, algorithm="HS256")
        }

    elif not user:
        answer = {
            "status": "error",
            "detail": "User doesn't exist."
        }
    
    else:
        answer = {
            "status": "error",
            "detail": "Passwords didn't match."
        }

    return answer


@app.route('/reg', methods=['POST'])
def user_registration():
    return jsonify(
        check_user_data_for_reg()
    )


@app.route('/auth', methods=['POST'])
def user_authentication():
    return jsonify(
        check_user_data_for_auth()
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
