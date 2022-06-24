from typing import Union
from psycopg2 import sql


class TableField:

    def __init__(self, field_name: str):
        self._name = field_name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    def as_(self, alias: str):
        return f'{self.name} AS {alias}'


class Table:

    def __init__(self, name: str, *fields: str):
        self._name = name
        self._make_fields(fields)

    def _make_fields(self, fields: tuple):
        for field in fields:
            self.__setattr__(field, TableField(f'{self.table_name}.{field}'))

    @property
    def table_name(self) -> str:
        return self._name

    def select(self, *fields: Union[TableField, str]) -> 'QueryBuilder':
        return QueryBuilder().select(self.table_name, tuple(str(field) for field in fields))

    def insert(self, fields_values: dict) -> 'QueryBuilder':
        return QueryBuilder().insert_values(self.table_name, fields_values)


class QueryBuilder:

    def __init__(self):
        self._query = None

    @property
    def query(self):
        return self._query

    def select(self, table_name: str, columns: tuple) -> 'QueryBuilder':
        if columns:
            self._query = sql.SQL("SELECT {columns} FROM {table}").format(
                table=sql.Identifier(table_name),
                columns=sql.SQL(", ").join([sql.SQL(str(col)) for col in columns])
            )
        else:
            self._query = sql.SQL("SELECT * FROM {table}").format(
                table=sql.Identifier(table_name)
            )
        return self

    def join_on(self, join_params: dict[Table: tuple[TableField]]) -> 'QueryBuilder':
        for table, foreign_keys in join_params.items():
            self._query += sql.SQL(" JOIN {table} ON {key_fld_1} = {key_fld_2}").format(
                table=sql.Identifier(table.table_name),
                key_fld_1=sql.SQL(str(foreign_keys[0])),
                key_fld_2=sql.SQL(str(foreign_keys[1])),
            )
        return self

    def where(self, where_params: dict) -> 'QueryBuilder':
        if where_params:
            self._query += sql.SQL(" WHERE ") + sql.SQL(" AND ").join([sql.SQL("{}={}").format(
                sql.SQL(identifier), sql.Literal(value)) for identifier, value in where_params.items()]
            )
        return self

    def insert_values(self, table_name: str, fields_values: dict) -> 'QueryBuilder':
        self._query = sql.SQL("INSERT INTO {table} ({columns}) VALUES ({values})").format(
            table=sql.Identifier(table_name),
            columns=sql.SQL(", ").join([sql.SQL(field) for field in fields_values.keys()]),
            values=sql.SQL(", ").join([sql.Literal(val) for val in fields_values.values()])
        )
        return self


def count(field) -> str:
    return f'COUNT({field})'
