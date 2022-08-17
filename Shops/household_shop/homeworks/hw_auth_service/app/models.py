from config import db


class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(120), nullable=False)
