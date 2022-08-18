import hashlib
import jwt
from uuid import uuid4
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict
from models import User


class UsersAuthService:
    def __init__(self, user_model: User, secret_key: str):
        self.user_model = user_model
        self.secret_key = secret_key

    def get_user(self, email: str) -> User or None:
        try:
            result = self.user_model.get(self.user_model.email == email)
        except DoesNotExist:
            result = None
        return result

    def create_user(self, user_credentials: dict) -> None:
        user_uuid = str(uuid4())
        new_user = self.user_model.create(
            email=user_credentials.get("email"),
            uuid=user_uuid,
            password=self._make_password_hash(user_credentials.get('password'), user_uuid)
        )
        new_user.save()

    def check_credentials(self, user_credentials: dict) -> str or None:
        result = None
        user = self.get_user(user_credentials.get('email'))
        if user:
            if user.password == self._make_password_hash(
                    user_credentials.get('password'),
                    user.uuid
            ):
                result = self._generate_token(user)
        return result

    def _make_password_hash(self, password: str, uuid: str) -> str:
        hashed_password = hashlib.md5(bytes(password + self.secret_key + uuid, encoding='utf-8'))
        return hashed_password.hexdigest()

    def _generate_token(self, user: User) -> str:
        return jwt.encode(payload=model_to_dict(user), key=self.secret_key, algorithm="HS256")
