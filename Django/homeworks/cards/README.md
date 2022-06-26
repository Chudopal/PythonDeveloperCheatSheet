1. Заведите джанго-проект bank
2. Добавьте в проект приложение cards
3. Сделайте модели для:
    - банковских карт(имеют номер(16 цифр), дату "годен до", пользователя карты, счет к которому привязаны, cvv код)
    - счетов(имеет iban(можете просто uuid использовать) и сумму на счете)
    - пользователей(имя, возраст, uuid)
4. Сделайте пользователя manager в PostgreSQL следующей командой:
    ```sql
    CREATE USER manager WITH ENCRYPTED PASSWORD 'manager';
    ```
5. Сделайте БД `bank_system`
6. Дайте новому пользователю права в новой базе данных командой:
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE bank_system TO manager;
    ```
7. Подключите postgres в ваш проект:
    ```python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'bank_system',
            'USER': 'manager',
            'PASSWORD': 'manager',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
8. PORT может оказаться у вас другим, его можно посмотреть в БД командой:
    ```sql
    SELECT setting FROM pg_settings WHERE name = 'port';
    ```
9. Сделайте миграции и создайте таблицы в БД
10. (extra) Сделайте так, чтобы пароль, пользователь и название БД брались из переменных окружения. В windows это можно задать переменные окружения только при запуске проекта, командой:
    ```
    cmd /c "set KEY=VAL & set KEY1=VAL1 & python manage.py runserver"
    ```
    после этого их можно получить из кода:
    ```python
    import os
    print(os.environ.get("KEY"))
    print(os.environ.get("KEY1"))
    ```
    Точно также сделайте со своими переменными пароля, названия БД и именем пользователя. В macos и linux есть специальная команда `export` для этих целей.
11. Добавьте несколько пользователей, несколько карт пользователей и счетов через оболочку джанго, открыть оболочку можно командой `python manage.py shell`
12. Добавьте:
    - url - `users/<str:user_uuid>/cards` для просмотра всех карт пользователя
    - url - `users/<str:user_uuid>/accounts` для просмотра всех счетов пользователя
