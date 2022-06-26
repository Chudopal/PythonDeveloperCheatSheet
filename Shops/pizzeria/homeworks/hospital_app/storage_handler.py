import psycopg2


class DBException(Exception):
    def __str__(self):
        return "Database error occurred"


class DBStorage:
    def __init__(self, **kwargs):
        self._host = kwargs.get('host', '127.0.0.1')
        self._user = kwargs.get('user', '')
        self._password = kwargs.get('password', '')
        self._dbname = kwargs.get('dbname')

    def execute(self, *sql_query) -> psycopg2:
        try:
            connector = psycopg2.connect(host=self._host, user=self._user, password=self._password, dbname=self._dbname)
            cursor = connector.cursor()
            for query in sql_query:
                cursor.execute(query)
            connector.commit()
            return self._format_response(cursor)
        except Exception as error:
            raise DBException(error)

    def _format_response(self, db_response: 'DB connection cursor'):
        columns = [item[0] for item in db_response.description]
        data = [dict(zip(columns, row)) for row in db_response.fetchall()]
        return data
