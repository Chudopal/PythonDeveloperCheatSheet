import sqlite3
from dataclasses import dataclass, asdict


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
        template = """UPDATE {table_name} SET exp_date={new_exp_date} WHERE number={card_number}"""
        _SQL = template.format(table_name=self.table, new_exp_date=new_exp_date, card_number=number)
        self.db_connection.execute(_SQL)

    def get(self, holder_name: str) -> list:
        template = """SELECT * FROM {table_name} WHERE holder_name='{holder_name}'"""
        _SQL = template.format(table_name=self.table, holder_name=holder_name)
        return self.db_connection.execute(_SQL).fetchall()


@dataclass
class Card:
    def __str__(self):
        template = f'Card number: {self.number}\n' \
                   f'Card holder: {self.holder_name}\n' \
                   f'Expiration date: {self.exp_date}\n' \
                   f'CVV: {self.cvv_code}'
        return template
    number: int
    holder_name: str
    exp_date: str
    cvv_code: int


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


connector = DBConnection('cards.db')
manager = CardManager(
    DataHandler(connector, "cards")
)

card_1 = Card(1111222233334444, 'mr.Smith', '10/25', 458)
card_2 = Card(5555666677778888, 'Ghost', '12/23', 467)
card_3 = Card(9999000011112222, 'Neo', '04/26', 450)
card_4 = Card(3333444455556666, 'Morpheus', '06/22', 649)

# _SQL = """CREATE TABLE cards (number INTEGER, holder_name TEXT, exp_date TEXT, cvv_code INTEGER)"""
# connector.execute(_SQL)

all_cards = manager.get_cards('Neo')
for card in all_cards:
    print(card)
