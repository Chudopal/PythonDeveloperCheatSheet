import re
import sqlite3
from dataclasses import dataclass, asdict


class ValidationError(Exception):
    """raises when data is not valid"""


class DBConnection:
    def __init__(self, database: str):
        self._database = database

    def execute(self, *sql_query: str) -> sqlite3.Cursor:
        db_connector = sqlite3.connect(self._database)
        cursor = db_connector.cursor()
        for item in sql_query:
            cursor.execute(item)
        db_connector.commit()
        return cursor


class DataHandler:
    def __init__(self, db_connection: DBConnection, table: str):
        self.db_connection = db_connection
        self.table = table

    def add(self, card: dict):
        template = """INSERT INTO {table_name} VALUES {values}"""
        values_template = "({number}, '{holder_name}', '{exp_date}', {cvv_code})"
        values = values_template.format(**card)
        _SQL = template.format(table_name=self.table, values=values)
        self.db_connection.execute(_SQL)

    def delete(self, number: int):
        template = """DELETE FROM {table_name} WHERE number={card_number}"""
        _SQL = template.format(table_name=self.table, card_number=number)
        self.db_connection.execute(_SQL)

    def update(self, number: int, new_exp_date: str):
        template = """UPDATE {table_name} SET exp_date='{new_exp_date}' WHERE number={card_number}"""
        _SQL = template.format(table_name=self.table, new_exp_date=new_exp_date, card_number=number)
        self.db_connection.execute(_SQL)

    def get(self, holder_name: str) -> list:
        template = """SELECT * FROM {table_name} WHERE holder_name='{holder_name}'"""
        _SQL = template.format(table_name=self.table, holder_name=holder_name)
        return self.db_connection.execute(_SQL).fetchall()


@dataclass
class Card:
    number: int
    holder_name: str
    exp_date: str
    cvv_code: int

    def __str__(self):
        template = f'Card number: {self.number}\n' \
                   f'Card holder: {self.holder_name}\n' \
                   f'Expiration date: {self.exp_date}\n' \
                   f'CVV: {self.cvv_code}'
        return template


class CardManager:
    def __init__(self, storage: DataHandler):
        self.storage = storage

    def add_card(self, *cards):
        for card in cards:
            self.storage.add(asdict(card))

    def delete_card(self, card: Card):
        self.storage.delete(card.number)

    def update_exp_date(self, card: Card, new_exp_date: str):
        self.storage.update(card.number, new_exp_date)

    def get_cards(self, holder_name: str) -> list[Card]:
        return [Card(*card) for card in self.storage.get(holder_name)]


def validators_factory(pattern, error):
    def validator(string):
        is_match = re.fullmatch(pattern, string)
        if is_match:
            return string
        else:
            raise ValidationError(error)

    return validator


card_number_validator = validators_factory(r"\d{16}", "Incorrect card number")
card_exp_date_validator = validators_factory(r"^(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})$", "Incorrect expiration date")
card_cvv_code_validator = validators_factory(r"\d{3}", "Incorrect expiration date")
card_holder_validator = validators_factory(r"\b([a-z ]+[ ]*)+", "Incorrect card holder name")


def card_creator(card_number: str, card_holder: str, exp_date: str, cvv_code: str) -> Card:
    try:
        card_params = {
            "number": int(card_number_validator(card_number)),
            "holder_name": card_holder_validator(card_holder).upper(),
            "exp_date": card_exp_date_validator(exp_date),
            "cvv_code": int(card_cvv_code_validator(cvv_code))
        }
        return Card(**card_params)
    except ValidationError as error:
        print(error)
