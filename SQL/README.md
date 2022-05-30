# SQL
1. [Базы данных](#db)
2. [SQLite](#sqlite)
3. [PostgreSQL](#postgres)

### <a name="bd">Базы дынных</a>
- Самый лучший способ сохранять данные пользователя, на данный момент, - это базы данных. В отличаи от файлов, которые тоже могут сохранять данные вашей программы, базы данных имеют множество преимуществ, а именно:
    - Разрешения - вы можете задать разрешения, по которым пользователи базы могут взаимодействовать с данными
    - Структурированность - данные хранятся не абы как, а в конкретных местах и определенным образом, и база данных дает этому гарантии
    - Легкость работы над данными - чтобы получить какие-то записи из БД, не нужно считывать оттуда все данные. БД дает удобные инструменты для сортировки, фильтровки и обновления данных
    - Защита данных - БД не так уж легко взломать и получить доступ к данным.
- В реляционных БД данные хранятся в таблицах. Чтобы однозначно определить данные в таблице, есть такое понятие как **первичный ключ**. По сути это уникальное ненулевое значение какой-то записи в таблице, например email, уникальный идентификатор, uuid.
- **Внешним ключем** является ссылка из поля одной таблицы на первичный ключ другой таблицы.

### <a name='sqlite'>Основные команды (SQLite3)</a>
- Для работы с БД, в Python есть встроенный модуль `sqlite3`, для работы с бд нужно создать подключение и получить курсор:
    ```python
    import sqlite3

    connection = sqlite3.connect("example.db") # создаем соединение
    cursor = connection.cursor() # получаем курсор
    ```
    курсор - это объект, через который мы будем делать операции с БД, касающиеся данных. Соединение - более общая концепция, дающее контроль над всем взаимодействием с БД, а не только над данными.
- Создание таблиц происходит с помощью команды `CREATE TABLE table_name(...);`:
    ```python
    # создаем таблицу со столбцами id, email, name
    cursor.execute("""
        CREATE TABLE users (id, email, name); 
    """)
    connection.commit() # сохраняем
    ```
    Однажды создав таблицу, мы не можем ее создать второй раз. Потому после запуска данных строк кода, их стоит закомментить, чтобы не получать  ошибку.
- Добавление записей делается с помощью команды `INSERT INTO table_name VALUES (...);`:
    ```python
    # добавляем записи пользователей в таблицу
    cursor.execute(
        """INSERT INTO users VALUES (1, "edefe", "alex");"""
    )
    cursor.execute(
        """INSERT INTO users VALUES (2, "edefe1", "vova");"""
    )
    cursor.execute(
        """INSERT INTO users VALUES (3, "edefe2", "bob");"""
    )
    cursor.execute(
        """INSERT INTO users VALUES (5, "edefe3", "alice");"""
    )

    # сохраняем изменения
    connection.commit()
    ```

- Получение данных делается при помощи команды `SELECT ... FROM table_name;`:
    ```python
    # запрос на получение всех данных
    cursor.execute("""
        SELECT * FROM users;
    """)

    # получение запрашиваемых данных
    data = cursor.fetchall()
    ```
    Или можно получать только определенные колонки из таблицы:
    ```python
    # запрос на получение имен
    cursor.execute("""
        SELECT name FROM users;
    """)

    # получение запрашиваемых данных
    data = cursor.fetchall()
    ```
- Можно фильтровать получаемые данные при помощи конструкции `WHERE ...;`:
    ```python
    # запрос на получение всех данных о пользователе с именем bob
    cursor.execute("""
        SELECT * FROM users WHERE name="bob";
    """)

    # получение запрашиваемых данных
    data = cursor.fetchall()
    ```
- Обновление данных происходит с помощью команды `UPDATE table_name SET column_name=value;`, чаще всего нужно еще добавлять условие, т.е. указать, какие именно записи нужно обновить при помощи `WHERE`:
    ```python
    # запрос на обновление email у пользователей с именем bob
    cursor.execute("""
        UPDATE users SET email="qqq" WHERE name="bob";
    """)

    # сохранение изменений
    connection.commit()
    ```
- Удаление данных происходит через команду `DELETE FROM table_name WHERE ...;`, если не написать `WHERE` в конце и не указать условия, то будут удалены все данные из таблицы:
    ```python
    # запрос удаления пользователя с именем bob
    cursor.execute("""
        DELETE FROM users WHERE name="bob";
    """)

    # сохранение изменений
    connection.commit()
    ```
- Посмотреть о SQLite подробнее можно [тут](https://coderlessons.com/tutorials/bazy-dannykh/vyuchit-sqlite/uchebnik-po-sqlite)

### <a name='postgres'>PostgreSQL</a>
- PostgreSQL(рус док: [тут](https://postgrespro.ru/docs), англ док: [тут](https://www.postgresql.org/docs/)) является одной из наиболее популярных систем управления базами данных. В отличаи от SQLite - это не файловая база данных, а серверная, значит что для своего функционирования создает отдельный сервер, к которому могут подключаться различные приложения или пользователи со своими разрешениями. Как установить почитать [тут](https://metanit.com/sql/postgresql/1.1.php)
- Основные команды остаются прежними:
    1. `CREATE TABLE table_name(params);` -- в постгрес необходимо конкретно указывать тип столбца. Весь список [тут](https://postgrespro.ru/docs/postgrespro/10/datatype).
    2. `INSERT INTO table_name(params) VALUES (params), (params) ...;` -- можно убрать params, но тогда номер вставляемого значения должен соответствовать номеру столбца и вставляемых значений должно быть не меньше количества столбцов.
    3. `SELECT params FROM table_name WHERE column_name=value;` -- получение значений из таблицы, у которых column_name = value.
    4. `UPDATE table_name SET column_name=value WHERE column_name=value1;` -- изменение значения column_name везде, где column_name = value1.
    5. `DELETE FROM table_name WHERE column_name=value;` -- удаление всех записей таблицы, у которых column_name = value.

- [Создание таблиц](https://postgrespro.ru/docs/postgresql/14/sql-createtable). Всегда необходимо указывать определенный тип, кроме того, можно указывать определенные ограничения при помощи команды `CHECK`. Создадим таблицу пользователей:
    1. Подключим расширение для uuid:
    ```sql
    CREATE EXTENSION "uuid-ossp";
    ```
    2. Создадим таблицу пользователей с автоматической генерацией uuid:
    ```sql
    CREATE TABLE users(
        uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY, -- uuid - является первичным ключем
        name CHARACTER VARYING(256), -- задали имя с макс длиной 256
        age SMALLINT CHECK(age > 18 AND age < 100) -- подобрали тип данных для возраста и сделали проверку на то, чтобы возраст был больше 18 и меньше 100
    );
    ```
    В столбцы с ограничениями попросту нельзя занести значения, которые не соответствуют ограничениям.
    3. Кроме uuid, как в предыдущем примере, можно использовать просто уникальное числовое значение, например 1,2,3,4... В postgres для этого также есть инструменты, которые вместо нас будут искать доступные свободные индекси и генерировать их. Перепишем предыдущий пример:
    ```sql
    CREATE TABLE users_test(
        id SERIAL PRIMARY KEY, -- uuid - является первичным ключем
        name CHARACTER VARYING(256), -- задали имя с макс длиной 256
        age SMALLINT CHECK(age > 18 AND age < 100) -- подобрали тип данных для возраста и сделали проверку на то, чтобы возраст был больше 18 и меньше 100
    );
    ```
    `SERIAL` - специальный тип, который автоматически генерирует целочисленное значение, которое в таблице еще не занято. Однако дальше мы будем использовать первый вариант данной таблицы.
    4. Создадим еще одну таблицу, которая нам понадобится в будущем:
    ```sql
    CREATE TABLE projects(
        id SERIAL PRIMARY KEY,
        name VARCHAR (124),
        description TEXT
    );
    ```
- Для внесения данных в таблицу используется конструкция `INSERT`:
    ```sql
    INSERT INTO users(name, age)
    VALUES
    ('Bob', 23),
    ('Alice', 34),
    ('Karl', 45);
    ```
    Если попытаться внести пользователя с возрастом 120, будет ошибка, так как сработает ограничение, которое мы поставили.
    Добавим также данных во вторую таблицу:
    ```sql
    INSERT INTO projects(name, description)
    VALUES
    ('shop', 'Create an online shop'),
    ('bot', 'Create a telegram bot for buying products from online shop'),
    ('sql', 'Create some sql tasks');
    ```
- `SELECT` служит для получения данных из таблицы:
```sql
-- получение всех пользователей старше 30
SELECT name, age FROM users WHERE age > 30;
```
Кроме того иногда полезными являются [подзапросы](https://metanit.com/sql/postgresql/4.7.php):
```sql
-- получение всех пользователей, которые старше среднего
SELECT name, age FROM users WHERE age > (SELECT AVG(age) FROM users);

-- получение всех пользователей, которые старше чем разница между возрастом самого старого и самого молодого пользователя
SELECT name, age FROM users 
WHERE age > (
    SELECT MAX(age) - MIN(age) FROM users);
```
- Соединение таблиц.
    1. Создадим 3ю таблицу, на основе двух других:
    ```sql
    CREATE TABLE participants (
        user_uuid uuid REFERENCES users(uuid),
        project_id SERIAL REFERENCES projects(id),
        project_role CHARACTER VARYING(64) 
    );
    ```
    Эта таблица-связка между таблицами projects и users. Связывается она с ними при помощи внешнего ключа. Внешнию ключи объявляются при помощи ключевого слова `REFERENCES` и указанием таблицы и поля, на которое идет ссылка. Почитать [тут](https://metanit.com/sql/postgresql/2.5.php), дока [тут](https://postgrespro.ru/docs/postgresql/9.5/ddl-constraints#ddl-constraints-fk)
    
    2. Заполним таблицу на основе таблицы users:
    ```sql
    INSERT INTO participants
    SELECT uuid, 1, 'developer' -- можно делать так. берем uuid прямо налету и сразу вставляем в participants
    FROM users WHERE name='Bob';

    INSERT INTO participants
    SELECT uuid, 2, 'developer'
    FROM users WHERE name='Bob';

    INSERT INTO participants
    SELECT uuid, 3, 'developer'
    FROM users WHERE name='Bob';

    INSERT INTO participants
    SELECT uuid, 2, 'team-lead'
    FROM users WHERE name='Alice';

    INSERT INTO participants
    SELECT uuid, 3, 'project manager'
    FROM users WHERE name='Karl';
    ```
    3. Теперь сделаем запросы во все 3 таблицы сразу, соединяя их:
    ```sql
    -- получить названия проектов, и роль, в которых есть Bob
    SELECT projects.name, project_role
    FROM users JOIN participants
    ON users.uuid = participants.user_uuid
    JOIN projects
    ON participants.project_id = projects.id
    WHERE users.name = 'Bob';

    --(extra) получить проекты, на которых средний возраст всех участников ниже, чем средний возраст в компании
    WITH project_age AS (
        SELECT projects.name as project_name,
        AVG(users.age) as user_age
        FROM users JOIN participants
        ON users.uuid = participants.user_uuid
        JOIN projects
        ON participants.project_id = projects.id
        GROUP BY project_name
    )
    SELECT project_name, user_age
    FROM project_age
    WHERE user_age < (SELECT AVG(age) FROM users);
    ```
    О соединении таблиц почитать [тут](https://metanit.com/sql/postgresql/6.3.php).(extra) Последний запрос с `WITH` называется называется общим табличным выражением(CTE). Почитать можно очень интересно можно [тут](https://habr.com/ru/company/postgrespro/blog/451344/), дока [тут](https://postgrespro.ru/docs/postgresql/9.5/queries-with)