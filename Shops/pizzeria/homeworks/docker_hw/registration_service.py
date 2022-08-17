import json
import hashlib


class JsonStorage:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def read(self) -> list:
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)
        except OSError:
            data = []
        return data

    def save(self, data: list) -> None:
        with open(self.file_name, "w") as file:
            json.dump(data, file)


class Users:
    def __init__(self, storage_file: str, secret_key: str):
        self.storage = JsonStorage(storage_file)
        self.secret_key = secret_key

    def get_user(self, email: str) -> dict or None:
        users = self.storage.read()
        result = None
        for user in users:
            if user.get('email') == email:
                result = user
        return result

    def save_user(self, user: dict) -> None:
        hashed_password = self._make_password_hash(user.get('password'))
        user.update({'password': hashed_password})
        all_users = self.storage.read()
        all_users.append(user)
        self.storage.save(all_users)

    def check_credentials(self, user_credentials: dict) -> str or None:
        result = None
        user = self.get_user(user_credentials.get('email'))
        if user:
            if user.get('password') == self._make_password_hash(user_credentials.get('password')):
                result = self._generate_token(user_credentials)
        return result

    def _make_password_hash(self, password: str) -> str:
        hashed_password = hashlib.md5(bytes(password + self.secret_key, encoding='utf-8'))
        return hashed_password.hexdigest()

    def _generate_token(self, user_credentials: dict) -> str:
        return "Token should be here"
