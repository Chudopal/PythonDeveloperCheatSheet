from flask_api import status
from models import User
from config import db
import hashlib
import jwt


class RegService:
    def __init__(self, request_json) -> None:
        self.email = request_json.get("Email")
        self.password = request_json.get("Password")

    def _get_md5_password(self):    
        md5_hash = hashlib.md5()
        md5_hash.update(bytes(self.password, 'utf-8'))
        return md5_hash.hexdigest()

    def credentials_ctrl(self):
        if not self.email or not self.password:
            return status.HTTP_203_NON_AUTHORITATIVE_INFORMATION

    def check_user_data_for_reg(self):
        if not User.query.get(self.email):
            db.session.add(
                User(email=self.email, password=self._get_md5_password())
            )
            db.session.commit()
            
            answer = {status.HTTP_201_CREATED: {"status": "ok"}}
        else:
            answer = {status.HTTP_400_BAD_REQUEST: {
                "status": "error",
                "detail": "User already exists."
            }}
        
        return answer

    def check_user_data_for_auth(self):
        user = User.query.get(self.email)

        if not user:
            answer = {status.HTTP_400_BAD_REQUEST: {
                "status": "error",
                "detail": "User doesn't exist."
            }}

        elif user.password == self._get_md5_password():   
            answer = {status.HTTP_200_OK: {
                "status": "ok",
                "token": jwt.encode({"some": "payload"}, self.email, algorithm="HS256")
            }}

        else:
            answer = {status.HTTP_400_BAD_REQUEST: {
                "status": "error", 
                "detail": "Passwords didn't match.",
                "wd": user.password
            }}

        return answer
