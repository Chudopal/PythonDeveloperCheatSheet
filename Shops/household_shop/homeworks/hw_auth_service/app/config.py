from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

answer_by_code = {
    201: {
        "status": "ok"
    },
    200: {
        "status": "ok",
        "token": ""
    },
    400: {
        "already_exists": {
            "status": "error",
            "detail": "User already exists."
        },
        "Passwords_ctrl": {
            "status": "error",
            "detail": "Passwords didn't match."
        },
        "User_doesn't_exist": {
            "satus": "error",
            "detail": "User doesn't exist."
        }
    },
    "Credential": {
        "error": "Please check your Login Credential and/or access rights"
    }
}
