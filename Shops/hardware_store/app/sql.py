import psycopg2
from contextlib import closing
from psycopg2.extras import DictCursor
from psycopg2 import sql


text = input('Введите колонку')

with closing(psycopg2.connect(dbname='banking_system', user='postgres',
                              password='mypassword', host='localhost')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        columns = (text,)
        stmt = sql.SQL('SELECT {} FROM {} LIMIT 5').format(
            sql.SQL(',').join(map(sql.Identifier, columns)),
            sql.Identifier('shop_invent')
        )
        cursor.execute(stmt)
        for row in cursor:
            print(row)
